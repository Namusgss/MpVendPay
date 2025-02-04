# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, EmailStr
# from pymongo import MongoClient
# import socket

# # Initialize FastAPI app
# app = FastAPI()

# # MongoDB Connection
# MONGO_URI = "mongodb://localhost:27017"  # Replace with your MongoDB URI
# DATABASE_NAME = "vendme"
# PRODUCT_COLLECTION_NAME = "productdetails"  # Collection for product details
# USER_COLLECTION_NAME = "userdata"  # Collection for user data

# client = MongoClient(MONGO_URI)
# db = client[DATABASE_NAME]
# product_collection = db[PRODUCT_COLLECTION_NAME]
# user_collection = db[USER_COLLECTION_NAME]

# # MongoDB URI and collection names
# # MONGO_URI = "mongodb://localhost:27017"  # Replace with your MongoDB URI
# # DATABASE_NAME = "vendme"
# # PRODUCT_COLLECTION_NAME = "productdetails"  # Collection for product details
# # USER_COLLECTION_NAME = "userdata"  # Collection for user data

# # client = AsyncIOMotorClient(MONGO_URI)
# # db = client[DATABASE_NAME]
# # product_collection = db[PRODUCT_COLLECTION_NAME]
# # user_collection = db[USER_COLLECTION_NAME]

# # Pydantic Models
# class UserCreate(BaseModel):
#     username: str
#     password: str  # Store passwords as plaintext
#     email: EmailStr
#     number: str

# class UserLogin(BaseModel):
#     username: str
#     password: str

# # Function to check if user exists
# def get_user_by_username(username: str):
#     return user_collection.find_one({"username": username})

# def get_user_by_email(email: str):
#     return user_collection.find_one({"email": email})

# # Register User Endpoint
# @app.post("/register")
# async def register_user(user: UserCreate):
#     if get_user_by_email(user.email):
#         raise HTTPException(status_code=400, detail="Email already registered.")
#     if get_user_by_username(user.username):
#         raise HTTPException(status_code=400, detail="Username already taken.")

#     # Insert user into database (storing password as plaintext)
#     user_data = {
#         "username": user.username,
#         "email": user.email,
#         "password": user.password,  # Storing as plaintext
#         "number": user.number
#     }
#     user_collection.insert_one(user_data)

#     return {"message": "User registered successfully"}

# # Login User Endpoint
# @app.post("/login")
# async def login_user(user: UserLogin):
#     db_user = get_user_by_username(user.username)

#     if not db_user:
#         raise HTTPException(status_code=400, detail="Invalid username")
    
#     if user.password != db_user["password"]:
#         raise HTTPException(status_code=400, detail="Invalid password")

#     return {"message": "Login successful"}

# # Route to fetch all users (for testing purposes)
# @app.get("/users")
# async def get_users():
#     docs = await user_collection.find().to_list(100)
#     return [serialize_user_doc(doc) for doc in docs]

# # Root endpoint for testing
# @app.get("/")
# async def root():
#     return {"message": "FastAPI with MongoDB is running!"}

# # Print the actual IP and accessible address on startup
# @app.on_event("startup")
# async def on_startup():
#     hostname = socket.gethostname()
#     local_ip = socket.gethostbyname(hostname)
#     print(f"API is running! Access it at http://{local_ip}:8000")

# running code


# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, EmailStr
# from pymongo import MongoClient
# import socket
# from passlib.context import CryptContext

# # Initialize FastAPI app
# app = FastAPI()

# # MongoDB Connection
# MONGO_URI = "mongodb://localhost:27017"  # Replace with your MongoDB URI
# DATABASE_NAME = "vendme"
# PRODUCT_COLLECTION_NAME = "productdetails"
# USER_COLLECTION_NAME = "userdata"

# client = MongoClient(MONGO_URI)
# db = client[DATABASE_NAME]
# product_collection = db[PRODUCT_COLLECTION_NAME]
# user_collection = db[USER_COLLECTION_NAME]


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


# # Password hashing
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # Pydantic Models
# class UserCreate(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     number: str

# class UserLogin(BaseModel):
#     username: str
#     password: str

# # Helper functions
# def get_user_by_username(username: str):
#     return user_collection.find_one({"username": username})

# def get_user_by_email(email: str):
#     return user_collection.find_one({"email": email})

# def hash_password(password: str) -> str:
#     return pwd_context.hash(password)

# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return pwd_context.verify(plain_password, hashed_password)





# # Register User Endpoint
# @app.post("/register")
# async def register_user(user: UserCreate):
#     if get_user_by_email(user.email):
#         raise HTTPException(status_code=400, detail="Email already registered.")
#     if get_user_by_username(user.username):
#         raise HTTPException(status_code=400, detail="Username already taken.")

#     # Hash password before storing
#     hashed_password = hash_password(user.password)

#     user_data = {
#         "username": user.username,
#         "email": user.email,
#         "password": hashed_password,  # Store hashed password
#         "number": user.number
#     }
#     user_collection.insert_one(user_data)

#     return {"message": "User registered successfully"}

# # Login User Endpoint
# @app.post("/login")
# async def login_user(user: UserLogin):
#     db_user = get_user_by_username(user.username)

#     if not db_user:
#         raise HTTPException(status_code=400, detail="Invalid username")
    
#     if not verify_password(user.password, db_user["password"]):
#         raise HTTPException(status_code=400, detail="Invalid password")

#     return {"message": "Login successful" ,"username": db_user["username"]}

# # Route to fetch all users (for testing purposes)
# @app.get("/users")
# async def get_users():
#     users = list(user_collection.find({}, {"_id": 0}))  # Exclude MongoDB _id field
#     return users

# # Root endpoint for testing
# @app.get("/")
# async def root():
#     return {"message": "FastAPI with MongoDB is running!"}

# # Print the actual IP and accessible address on startup
# @app.on_event("startup")
# async def on_startup():
#     hostname = socket.gethostname()
#     local_ip = socket.gethostbyname(hostname)
#     print(f"API is running! Access it at http://{local_ip}:8000")


# new code with camera
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from pymongo import MongoClient
import socket

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

    # Model for storing transactions
class PurchaseRecord(BaseModel):
    username: str
    productName: str
    quantity: int
    amount: float

    # Save transaction after successful payment
@app.post("/save_transaction")
async def save_transaction(transaction: PurchaseRecord):
    history_collection.insert_one(transaction.dict())
    return {"message": "Transaction saved successfully"}

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

# Print the actual IP and accessible address on startup
@app.on_event("startup")
async def on_startup():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"API is running! Access it at http://{local_ip}:8000")
