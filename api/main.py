
# #new code with camera
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from pymongo import MongoClient
from datetime import datetime
import socket
import random
from uuid import uuid4 
from datetime import datetime, timedelta

# Temporary in-memory transaction flags to manage active transactions
transaction_flags = {}

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
    transactionId: str

class DispenseRequest(BaseModel):
    productName: str
    quantity: int

# Model for storing transactions
class PurchaseRecord(BaseModel):
    username: str
    productName: str
    quantity: int
    amount: float
    transactionDate: str  # Separate date field (YYYY-MM-DD)
    transactionTime: str  # Separate time field (HH:MM:SS)
    transactionId: str
    
class LoadBalanceRequest(BaseModel):
    username: str  # ✅ Only requires username

class UpdateDatabase(BaseModel):
    prouctName: str
    quantity: int

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
    print(f"✅ Login successful for {db_user['username']}")  # Debugging print
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


@app.get("/get_inventory")
async def get_inventory():
    try:
        # Fetch all products from the inventory collection
        inventory = list(product_collection.find())  # Use the correct collection name

        if not inventory:
            return {"message": "No products found"}

        # Return product details
        return [
            {
                "productName": product.get("name", "N/A"),
                "quantity": product.get("quantity", 0),
                "price": product.get("price", 0.0),
                "imageUrl": product.get("image", ""),
            }
            for product in inventory
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Process Payment (Deduct from Database)
@app.post("/process_payment")
async def process_payment(request: PaymentRequest):
    username = request.username.strip().lower()
    transaction_id = request.transactionId
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


# Save transaction after successful payment
 # For generating unique transaction IDs
@app.post("/save_transaction")
async def save_transaction(transaction: PurchaseRecord):
    try:
        transaction_data = {
            "transaction_id": transaction.transactionId,  
            "username": transaction.username,
            "productName": transaction.productName,
            "quantity": transaction.quantity,
            "amount": transaction.amount,
            "transactionDate": transaction.transactionDate,  # YYYY-MM-DD
            "transactionTime": transaction.transactionTime,  # HH:MM:SS AM/PM
        }

        # Insert transaction into the database
        result = history_collection.insert_one(transaction_data)

        if not result.inserted_id:
            raise HTTPException(status_code=500, detail="Failed to save transaction")

        return {"message": "Transaction saved successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
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

    # ✅ Find the latest unpaid transaction and mark it as paid
    latest_transaction = history_collection.find_one(
        sort=[("transactionDate", -1), ("transactionTime", -1)]
    )

    if latest_transaction:
        history_collection.update_one(
            {"_id": latest_transaction["_id"]},
        )
        return {"message": "Payment processed successfully", "transaction_id": latest_transaction["transaction_id"]}

    return {"message": "No pending transactions found"}



@app.get("/check_payment_status")
async def check_payment_status(username: str, transactionId: str):
    """Compare the provided transaction ID with the latest one in the database."""
    
    # Fetch the latest transaction for the user
    latest_transaction = history_collection.find_one(
        {"username": username},
        sort=[("transactionDate", -1), ("transactionTime", -1)]  # Get the latest transaction
    )
    print(transactionId)
   

    if not latest_transaction:
        return {"status": "no_transaction", "message": "No transaction found"}

    stored_transaction_id = latest_transaction.get("transaction_id", None)
    print(stored_transaction_id)
    # Compare provided transaction ID with stored transaction ID
    if stored_transaction_id  == transactionId:
                return {"status": "success", "product": latest_transaction["productName"]}
 
    else:
        return {"status": "pending", "message": "Payment is pending"}

from fastapi import Request

@app.post("/update_database")
async def update_database(request: Request):  # Request object to manually extract JSON
    data = await request.json()  # Extract JSON data
    product_name = data.get("productName")  # Extract productName
    quantity_sold = data.get("quantity")  # Extract quantity
    
    print("Received Data:", data)  # Debugging

    if not product_name or quantity_sold is None:
        return {"error": "Invalid data received"}

    # Find the product in the database
    product = product_collection.find_one({"name": product_name})
    print("Product Found:", product)

    if product:
        current_quantity = int(product['quantity'])
        print("Quantity Sold:", quantity_sold, "Type:", type(quantity_sold))  # Debugging

        # Subtract the quantity from the current stock
        new_quantity = current_quantity - quantity_sold

        if new_quantity < 0:
            return {"error": "Not enough stock available"}
        
        # Update the product quantity in the database
        result = product_collection.update_one(
            {"name": product_name},
            {"$set": {"quantity": new_quantity}}
        )

        if result.modified_count > 0:
            return {"message": f"Successfully updated quantity for {product_name}"}
        else:
            return {"error": "Failed to update quantity"}
    else:
        return {"error": "Product not found"}


# Fetch user's purchase history
@app.get("/get_purchase_history")
async def get_purchase_history(username: str):
    transactions = list(history_collection.find({"username": username}).sort([("transactionDate", -1), ("transactionTime", -1)]))
    print("Transactions:", transactions)  # Log all transactions to check for missing fields
    
    if not transactions:
        return {"message": "No transactions found"}

    return [
        {
            "productName": t.get("productName", "N/A"),  # Use .get() to avoid key errors
            "quantity": t.get("quantity", 0),
            "amount": t.get("amount", 0.0),
            "transactionDate": t.get("transactionDate", "N/A"),  # Use .get() to avoid key errors
            "transactionTime": t.get("transactionTime", "N/A"),  # Use .get() to avoid key errors
        }
        for t in transactions
    ]



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

