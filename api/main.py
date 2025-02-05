
# new code with camera
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from pymongo import MongoClient
import socket
import random

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change for production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017"  # Replace with your MongoDB URI
DATABASE_NAME = "vendme"
PRODUCT_COLLECTION_NAME = "productdetails"
USER_COLLECTION_NAME = "userdata"
HISTORY_COLLECTION_NAME = "purchase_history"

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
product_collection = db[PRODUCT_COLLECTION_NAME]
users_collection = db[USER_COLLECTION_NAME]
history_collection = db[HISTORY_COLLECTION_NAME]



# Helper to serialize MongoDB documents for products
def serialize_product_doc(doc):
    return {
        "id": str(doc["_id"]),  # Convert ObjectId to string
        "name": doc.get("name", ""),
        "price": doc.get("price", 0.0),
        "quantity": doc.get("quantity", 0),
        "image": doc.get("image", ""),
    }

@app.get("/items")
async def get_items():
    docs = list(product_collection.find())  # Fetch all documents
    return [serialize_product_doc(doc) for doc in docs]

# Pydantic Models
class UserCreate(BaseModel):
    username: str
    password: str
    email: EmailStr
    number: str

class UserLogin(BaseModel):
    username: str
    password: str

class PaymentRequest(BaseModel):
    username: str
    amount: float

class DispenseRequest(BaseModel):
    productName: str
    quantity: int

# Model for storing transactions
class PurchaseRecord(BaseModel):
    username: str
    productName: str
    quantity: int
    amount: float

class LoadBalanceRequest(BaseModel):
    username: str  # ✅ Only requires username
# Function to get user by username
def get_user_by_username(username: str):
    return users_collection.find_one({"username": username.strip().lower()})  # ✅ Normalize username to lowercase

# Register User Endpoint
@app.post("/register")
async def register_user(user: UserCreate):
    username = user.username.strip().lower()  # Normalize username
    
    if get_user_by_username(username):
        raise HTTPException(status_code=400, detail="Username already taken.")

    user_data = {
        "username": username,
        "email": user.email.strip().lower(),
        "password": user.password,
        "number": user.number.strip(),
        "balance": 100.00  # Default balance for new users
    }
    users_collection.insert_one(user_data)
    return {"message": "User registered successfully"}

# Login User Endpoint
@app.post("/login")
async def login_user(user: UserLogin):
    username = user.username.strip().lower()
    db_user = get_user_by_username(username)

    if not db_user or user.password != db_user["password"]:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    return {"message": "Login successful"}

# Fetch User Balance
@app.get("/get_balance")
async def get_balance(username: str):
    username = username.strip().lower()  # Ensure consistency
    user = get_user_by_username(username)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    balance = user.get("balance", 0.00)  # Default to $0.00 if balance is missing
    return {"balance": balance}

# Process Payment (Deduct from Database)
@app.post("/process_payment")
async def process_payment(request: PaymentRequest):
    username = request.username.strip().lower()
    
    user = get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    current_balance = user.get("balance", 0.00)

    if current_balance < request.amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    # Deduct amount and update balance in MongoDB
    new_balance = current_balance - request.amount
    users_collection.update_one(
        {"username": username},
        {"$set": {"balance": new_balance}}
    )
    return {"message": "Payment processed successfully", "new_balance": new_balance}

    

#     # Save transaction after successful payment
# @app.post("/save_transaction")
# async def save_transaction(transaction: PurchaseRecord):
#     print("Transaction Data Received:", transaction.dict())  # Log the transaction data
#     history_collection.insert_one(transaction.dict())
#     return {"message": "Transaction saved successfully"}

# # Save transaction after successful payment
@app.post("/save_transaction")
async def save_transaction(transaction: PurchaseRecord):
    try:
        # Log the received transaction data
        print("Transaction Data Received:", transaction)

        # Manually construct a dictionary from the Pydantic model attributes
        transaction_data = {
            "username": transaction.username,
            "productName": transaction.productName,
            "quantity": transaction.quantity,
            "amount": transaction.amount,
        }

        # Insert into the database
        result = history_collection.insert_one(transaction_data)

        if not result.inserted_id:
            raise HTTPException(status_code=500, detail="Failed to save transaction")

        return {"message": "Transaction saved successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

# Fetch user's purchase history
@app.get("/get_purchase_history")
async def get_purchase_history(username: str):
    transactions = list(history_collection.find({"username": username}))
    if not transactions:
        return {"message": "No transactions found"}

    return [
        {
            "productName": t["productName"],
            "quantity": t["quantity"],
            "amount": t["amount"],
        }
        for t in transactions
    ]


# Simulate Vending Machine Dispensing Product
@app.post("/dispense_product")
async def dispense_product(request: DispenseRequest):
    message = f"{request.quantity}x {request.productName} coming out of vending machine... brrrr ⚙️"
    
    print(message)  # Simulate hardware action
    return {"message": message}

# Add a Load Balance endpoint to randomly add money to user's balance
@app.post("/load_balance")
async def load_balance(request: LoadBalanceRequest):  # ✅ Use the new model
    username = request.username.strip().lower()
    
    user = get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Generate a random amount to add to the balance
    random_amount = round(random.uniform(10.0, 100.0), 2)

    # Update balance
    new_balance = user.get("balance", 0.00) + random_amount
    users_collection.update_one(
        {"username": username},
        {"$set": {"balance": new_balance}}
    )

    return {"message": f"Balance updated by {random_amount} NPR", "new_balance": new_balance}
    
# Print the actual IP and accessible address on startup
@app.on_event("startup")
async def on_startup():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"API is running! Access it at http://{local_ip}:8000")


# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel, EmailStr
# from pymongo import MongoClient
# import socket
# import random

# # Initialize FastAPI app
# app = FastAPI()

# # Enable CORS for frontend integration
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allow all origins (change for production)
#     allow_credentials=True,
#     allow_methods=["*"],  # Allow all HTTP methods
#     allow_headers=["*"],  # Allow all headers
# )

# # MongoDB Connection
# MONGO_URI = "mongodb://localhost:27017"  # Replace with your MongoDB URI
# DATABASE_NAME = "vendme"
# PRODUCT_COLLECTION_NAME = "productdetails"
# USER_COLLECTION_NAME = "userdata"
# HISTORY_COLLECTION_NAME = "purchase_history"

# client = MongoClient(MONGO_URI)
# db = client[DATABASE_NAME]
# product_collection = db[PRODUCT_COLLECTION_NAME]
# users_collection = db[USER_COLLECTION_NAME]
# history_collection = db[HISTORY_COLLECTION_NAME]

# # Helper to serialize MongoDB documents for products
# def serialize_product_doc(doc):
#     return {
#         "id": str(doc["_id"]),  # Convert ObjectId to string
#         "name": doc.get("name", ""),
#         "price": doc.get("price", 0.0),
#         "quantity": doc.get("quantity", 0),
#         "image": doc.get("image", ""),
#     }

# @app.get("/items")
# async def get_items():
#     docs = list(product_collection.find())  # Fetch all documents
#     return [serialize_product_doc(doc) for doc in docs]

# # Pydantic Models
# class UserCreate(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     number: str

# class UserLogin(BaseModel):
#     username: str
#     password: str

# class PaymentRequest(BaseModel):
#     username: str
#     amount: float
#     productName: str  # Added product name to PaymentRequest
#     quantity: int  # Added quantity to PaymentRequest

# class DispenseRequest(BaseModel):
#     productName: str
#     quantity: int

# class PurchaseRecord(BaseModel):
#     username: str
#     productName: str
#     quantity: int
#     amount: float

# class LoadBalanceRequest(BaseModel):
#     username: str

# # Function to get user by username
# def get_user_by_username(username: str):
#     return users_collection.find_one({"username": username.strip().lower()})

# # Register User Endpoint
# @app.post("/register")
# async def register_user(user: UserCreate):
#     username = user.username.strip().lower()
#     if get_user_by_username(username):
#         raise HTTPException(status_code=400, detail="Username already taken.")
    
#     user_data = {
#         "username": username,
#         "email": user.email.strip().lower(),
#         "password": user.password,
#         "number": user.number.strip(),
#         "balance": 100.00
#     }
#     users_collection.insert_one(user_data)
#     return {"message": "User registered successfully"}

# # Login User Endpoint
# @app.post("/login")
# async def login_user(user: UserLogin):
#     username = user.username.strip().lower()
#     db_user = get_user_by_username(username)
#     if not db_user or user.password != db_user["password"]:
#         raise HTTPException(status_code=400, detail="Invalid username or password")
#     return {"message": "Login successful"}

# # Fetch User Balance
# @app.get("/get_balance")
# async def get_balance(username: str):
#     username = username.strip().lower()
#     user = get_user_by_username(username)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return {"balance": user.get("balance", 0.00)}

# # Process Payment
# @app.post("/process_payment")
# async def process_payment(request: PaymentRequest):
#     username = request.username.strip().lower()
#     user = get_user_by_username(username)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
    
#     current_balance = user.get("balance", 0.00)
#     if current_balance < request.amount:
#         raise HTTPException(status_code=400, detail="Insufficient balance")
    
#     new_balance = current_balance - request.amount
#     users_collection.update_one({"username": username}, {"$set": {"balance": new_balance}})
    
#     # Save the transaction to the purchase history
#     purchase_record = PurchaseRecord(
#         username=username,
#         productName=request.productName,  # Passed product name from request
#         quantity=request.quantity,        # Passed quantity from request
#         amount=request.amount
#     )
#     await save_transaction(purchase_record)  # Calling the function to save the transaction
    
#     return {"message": "Payment processed and transaction saved successfully", "new_balance": new_balance}

# # Save transaction after successful payment
# @app.post("/save_transaction")
# async def save_transaction(transaction: PurchaseRecord):
#     transaction_data = {
#         "username": transaction.username.strip().lower(),
#         "productName": transaction.productName,
#         "quantity": transaction.quantity,
#         "amount": transaction.amount,
#     }
#     result = history_collection.insert_one(transaction_data)
#     if not result.inserted_id:
#         raise HTTPException(status_code=500, detail="Failed to save transaction")
#     return {"message": "Transaction saved successfully"}

# # Fetch user's purchase history
# @app.get("/get_purchase_history")
# async def get_purchase_history(username: str):
#     transactions = list(history_collection.find({"username": username.strip().lower()}))
#     if not transactions:
#         return {"message": "No transactions found"}
#     return [{
#         "productName": t["productName"],
#         "quantity": t["quantity"],
#         "amount": t["amount"]
#     } for t in transactions]

# # Simulate Vending Machine Dispensing Product
# @app.post("/dispense_product")
# async def dispense_product(request: DispenseRequest):
#     return {"message": f"{request.quantity}x {request.productName} dispensed."}

# # Load Balance Endpoint
# @app.post("/load_balance")
# async def load_balance(request: LoadBalanceRequest):
#     username = request.username.strip().lower()
#     user = get_user_by_username(username)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     random_amount = round(random.uniform(10.0, 100.0), 2)
#     new_balance = user.get("balance", 0.00) + random_amount
#     users_collection.update_one({"username": username}, {"$set": {"balance": new_balance}})
#     return {"message": f"Balance updated by {random_amount} NPR", "new_balance": new_balance}

# # Print IP on startup
# @app.on_event("startup")
# async def on_startup():
#     hostname = socket.gethostname()
#     local_ip = socket.gethostbyname(hostname)
#     print(f"API is running! Access it at http://{local_ip}:8000")
