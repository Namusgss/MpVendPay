
# #new code with camera
# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel, EmailStr
# from pymongo import MongoClient
# from datetime import datetime
# import socket
# import random
# from datetime import datetime


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

# class DispenseRequest(BaseModel):
#     productName: str
#     quantity: int

# # Model for storing transactions
# class PurchaseRecord(BaseModel):
#     username: str
#     productName: str
#     quantity: int
#     amount: float
#     transactionDate: str  # Separate date field (YYYY-MM-DD)
#     transactionTime: str  # Separate time field (HH:MM:SS)
# class LoadBalanceRequest(BaseModel):
#     username: str  # ✅ Only requires username
# # Function to get user by username
# def get_user_by_username(username: str):
#     return users_collection.find_one({"username": username.strip().lower()})  # ✅ Normalize username to lowercase

# # Register User Endpoint
# @app.post("/register")
# async def register_user(user: UserCreate):
#     username = user.username.strip().lower()  # Normalize username
    
#     if get_user_by_username(username):
#         raise HTTPException(status_code=400, detail="Username already taken.")

#     user_data = {
#         "username": username,
#         "email": user.email.strip().lower(),
#         "password": user.password,
#         "number": user.number.strip(),
#         "balance": 100.00  # Default balance for new users
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
#     username = username.strip().lower()  # Ensure consistency
#     user = get_user_by_username(username)
    
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     balance = user.get("balance", 0.00)  # Default to $0.00 if balance is missing
#     return {"balance": balance}


# @app.get("/get_inventory")
# async def get_inventory():
#     try:
#         # Fetch all products from the inventory collection
#         inventory = list(product_collection.find())  # Use the correct collection name

#         if not inventory:
#             return {"message": "No products found"}

#         # Return product details
#         return [
#             {
#                 "productName": product.get("name", "N/A"),
#                 "quantity": product.get("quantity", 0),
#                 "price": product.get("price", 0.0),
#                 "imageUrl": product.get("image", ""),
#             }
#             for product in inventory
#         ]
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# # Process Payment (Deduct from Database)
# @app.post("/process_payment")
# async def process_payment(request: PaymentRequest):
#     username = request.username.strip().lower()
    
#     user = get_user_by_username(username)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     current_balance = user.get("balance", 0.00)

#     if current_balance < request.amount:
#         raise HTTPException(status_code=400, detail="Insufficient balance")

#     # Deduct amount and update balance in MongoDB
#     new_balance = current_balance - request.amount
#     users_collection.update_one(
#         {"username": username},
#         {"$set": {"balance": new_balance}}
#     )
#     return {"message": "Payment processed successfully", "new_balance": new_balance}


# # Save transaction after successful payment
# @app.post("/save_transaction")
# async def save_transaction(transaction: PurchaseRecord):
#     try:
#         # Log the received transaction data
#         print("Transaction Data Received:", transaction)

#         # Manually construct a dictionary from the Pydantic model attributes
#         transaction_data = {
#             "username": transaction.username,
#             "productName": transaction.productName,
#             "quantity": transaction.quantity,
#             "amount": transaction.amount,
#             "transactionDate": transaction.transactionDate,  # Save only date
#             "transactionTime": transaction.transactionTime,  # Save only time
#         }

#         # Insert into the database
#         result = history_collection.insert_one(transaction_data)

#         if not result.inserted_id:
#             raise HTTPException(status_code=500, detail="Failed to save transaction")

#         return {"message": "Transaction saved successfully"}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    

# # @app.get("/check_payment_status")
# # async def check_payment_status(username: str):
# #     # Look for the most recent purchase in the history
# #     transaction = history_collection.find_one(
# #         {"username": username},
# #         sort=[("transactionDate", -1), ("transactionTime", -1)]  # Get the latest transaction
# #     )

# #     if not transaction:
# #         raise HTTPException(status_code=404, detail="No transactions found for this user")

# #     # If the transaction is successful, return a success message
# #     if transaction["amount"] > 0:
# #         return {"status": "success", "product": transaction["productName"]}

# #     return {"status": "pending", "message": "Payment is pending"}

# # @app.get("/check_payment_status")
# # async def check_payment_status(username: str):
# #     try:
# #         # Find the latest transaction for the user
# #         transaction = history_collection.find_one(
# #             {"username": username},
# #             sort=[("transactionDate", -1), ("transactionTime", -1)]  # Get the latest transaction
# #         )

# #         if not transaction:
# #             return {"status": "pending", "message": "No transaction found for this user."}

# #         # If transaction exists, check the amount and payment status
# #         if int(transaction["amount"]) > 0 and transaction.get("payment_status") == "completed":
# #             return {"status": "success", "message": "Payment successful"}

# #         return {"status": "pending", "message": "Payment still pending"}

# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail=f"Error checking payment status: {str(e)}")

# @app.get("/check_payment_status")
# async def check_payment_status(username: str):
#     global transaction_done
#     try:
#         # Look for the most recent purchase in the history
#         transaction = history_collection.find_one(
#             {"username": username},
#             sort=[("transactionDate", -1), ("transactionTime", -1)]  # Get the latest transaction
#         )

#         if not transaction:
#             raise HTTPException(status_code=404, detail="No transactions found for this user")

#         # If the transaction is successful, return a success message
#         if int(transaction["amount"]) > 0 and transaction_done == True:
#             transaction_done = not transaction_done
#             return {"status": "success", "product": transaction["productName"]}

#         return {"status": "pending", "message": "Payment is pending"}
    
#     except Exception as e:
#         print(f"Error processing payment status for {username}: {e}")
#         raise HTTPException(status_code=500, detail="Server error while checking payment status")



# # Fetch user's purchase history
# @app.get("/get_purchase_history")
# async def get_purchase_history(username: str):
#     transactions = list(history_collection.find({"username": username}).sort([("transactionDate", -1), ("transactionTime", -1)]))
#     print("Transactions:", transactions)  # Log all transactions to check for missing fields
    
#     if not transactions:
#         return {"message": "No transactions found"}

#     return [
#         {
#             "productName": t.get("productName", "N/A"),  # Use .get() to avoid key errors
#             "quantity": t.get("quantity", 0),
#             "amount": t.get("amount", 0.0),
#             "transactionDate": t.get("transactionDate", "N/A"),  # Use .get() to avoid key errors
#             "transactionTime": t.get("transactionTime", "N/A"),  # Use .get() to avoid key errors
#         }
#         for t in transactions
#     ]



# # Add a Load Balance endpoint to randomly add money to user's balance
# @app.post("/load_balance")
# async def load_balance(request: LoadBalanceRequest):  # ✅ Use the new model
#     username = request.username.strip().lower()
    
#     user = get_user_by_username(username)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     # Generate a random amount to add to the balance
#     random_amount = round(random.uniform(10.0, 100.0), 2)

#     # Update balance
#     new_balance = user.get("balance", 0.00) + random_amount
#     users_collection.update_one(
#         {"username": username},
#         {"$set": {"balance": new_balance}}
#     )

#     return {"message": f"Balance updated by {random_amount} NPR", "new_balance": new_balance}
    
# # Print the actual IP and accessible address on startup
# @app.on_event("startup")
# async def on_startup():
#     hostname = socket.gethostname()
#     local_ip = socket.gethostbyname(hostname)
#     print(f"API is running! Access it at http://{local_ip}:8000")




# # # Add this to your existing FastAPI code
# # from fastapi import FastAPI, HTTPException
# # from fastapi.middleware.cors import CORSMiddleware
# # from pydantic import BaseModel, EmailStr
# # from pymongo import MongoClient
# # from datetime import datetime
# # import socket
# # import random
# # import sys
# # import time
# # from typing import Dict

# # # Conditional import for RPi.GPIO (only if on Raspberry Pi)
# # try:
# #     if sys.platform.startswith("linux"):  # Only imports RPi.GPIO on Linux systems
# #         import RPi.GPIO as GPIO
# #         GPIO.setmode(GPIO.BCM)
# # except ModuleNotFoundError:
# #     # Mock GPIO functionality when running on a non-Raspberry Pi system
# #     class MockGPIO:
# #         BOARD = BCM = OUT = IN = HIGH = LOW = None
# #         def setmode(self, mode): pass
# #         def setup(self, pin, mode): pass
# #         def output(self, pin, state): pass
# #         def input(self, pin): return 0
# #         def cleanup(self): pass

# #     GPIO = MockGPIO()
# #     print("Running in mock mode: RPi.GPIO not available on this platform.")

# # # Initialize FastAPI app
# # app = FastAPI()

# # # Enable CORS for frontend integration
# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["*"],
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# # # MongoDB Connection
# # MONGO_URI = "mongodb://localhost:27017"
# # DATABASE_NAME = "vendme"
# # PRODUCT_COLLECTION_NAME = "productdetails"
# # USER_COLLECTION_NAME = "userdata"
# # HISTORY_COLLECTION_NAME = "purchase_history"

# # client = MongoClient(MONGO_URI)
# # db = client[DATABASE_NAME]
# # product_collection = db[PRODUCT_COLLECTION_NAME]
# # users_collection = db[USER_COLLECTION_NAME]
# # history_collection = db[HISTORY_COLLECTION_NAME]

# # # Motor pin configuration
# # MOTOR_PINS = {
# #     "noodles": 18,
# #     "chips": 23
# # }

# # # Setup GPIO
# # for pin in MOTOR_PINS.values():
# #     GPIO.setup(pin, GPIO.OUT)
# #     GPIO.output(pin, GPIO.LOW)  # Ensure motors are off at start

# # class MotorController:
# #     @staticmethod
# #     def dispense_product(product_name: str) -> bool:
# #         try:
# #             if product_name.lower() not in MOTOR_PINS:
# #                 raise ValueError(f"Invalid product: {product_name}. Must be 'noodles' or 'chips'")

# #             pin = MOTOR_PINS[product_name.lower()]

# #             # Dispensing sequence
# #             GPIO.output(pin, GPIO.HIGH)

# #             # Adjust timing based on product
# #             if product_name.lower() == "noodles":
# #                 time.sleep(1.5)
# #             else:  # chips
# #                 time.sleep(1.0)

# #             GPIO.output(pin, GPIO.LOW)
# #             time.sleep(0.5)  # Wait for product to fully dispense

# #             return True

# #         except Exception as e:
# #             print(f"Error dispensing {product_name}: {e}")
# #             if 'pin' in locals():
# #                 GPIO.output(pin, GPIO.LOW)  # Safety: ensure motor is off
# #             return False

# # # Helper to serialize MongoDB documents
# # def serialize_product_doc(doc):
# #     return {
# #         "id": str(doc["_id"]),
# #         "name": doc.get("name", ""),
# #         "price": doc.get("price", 0.0),
# #         "quantity": doc.get("quantity", 0),
# #         "image": doc.get("image", ""),
# #     }

# # # Pydantic Models
# # class UserCreate(BaseModel):
# #     username: str
# #     password: str
# #     email: EmailStr
# #     number: str

# # class UserLogin(BaseModel):
# #     username: str
# #     password: str

# # class PaymentRequest(BaseModel):
# #     username: str
# #     amount: float
# #     productName: str
# #     quantity: int

# # class DispenseRequest(BaseModel):
# #     productName: str
# #     quantity: int

# # class PurchaseRecord(BaseModel):
# #     username: str
# #     productName: str
# #     quantity: int
# #     amount: float
# #     transactionDate: str
# #     transactionTime: str

# # class LoadBalanceRequest(BaseModel):
# #     username: str

# # # User Management Functions
# # def get_user_by_username(username: str):
# #     return users_collection.find_one({"username": username.strip().lower()})

# # @app.post("/register")
# # async def register_user(user: UserCreate):
# #     username = user.username.strip().lower()

# #     if get_user_by_username(username):
# #         raise HTTPException(status_code=400, detail="Username already taken.")

# #     user_data = {
# #         "username": username,
# #         "email": user.email.strip().lower(),
# #         "password": user.password,
# #         "number": user.number.strip(),
# #         "balance": 100.00
# #     }
# #     users_collection.insert_one(user_data)
# #     return {"message": "User registered successfully"}

# # @app.post("/login")
# # async def login_user(user: UserLogin):
# #     username = user.username.strip().lower()
# #     db_user = get_user_by_username(username)

# #     if not db_user or user.password != db_user["password"]:
# #         raise HTTPException(status_code=400, detail="Invalid username or password")

# #     return {"message": "Login successful"}

# # @app.get("/get_balance")
# # async def get_balance(username: str):
# #     username = username.strip().lower()
# #     user = get_user_by_username(username)

# #     if not user:
# #         raise HTTPException(status_code=404, detail="User not found")

# #     balance = user.get("balance", 0.00)
# #     return {"balance": balance}

# # @app.get("/get_inventory")
# # async def get_inventory():
# #     try:
# #         inventory = list(product_collection.find())

# #         if not inventory:
# #             return {"message": "No products found"}

# #         return [
# #             {
# #                 "productName": product.get("name", "N/A"),
# #                 "quantity": product.get("quantity", 0),
# #                 "price": product.get("price", 0.0),
# #                 "imageUrl": product.get("image", ""),
# #             }
# #             for product in inventory
# #         ]
# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail=str(e))

# # @app.post("/verify_payment")
# # async def verify_payment(payment_data: dict):
# #     try:
# #         username = payment_data.get("username")
# #         amount = payment_data.get("amount")
# #         product_name = payment_data.get("productName").lower()
# #         quantity = payment_data.get("quantity", 1)

# #         if product_name not in ["noodles", "chips"]:
# #             raise HTTPException(status_code=400, detail="Invalid product selection")

# #         user = get_user_by_username(username)
# #         if not user:
# #             raise HTTPException(status_code=404, detail="User not found")

# #         if user.get("balance", 0) < amount:
# #             raise HTTPException(status_code=400, detail="Insufficient balance")

# #         # Process payment
# #         new_balance = user["balance"] - amount
# #         users_collection.update_one(
# #             {"username": username},
# #             {"$set": {"balance": new_balance}}
# #         )

# #         # Update inventory
# #         product = product_collection.find_one({"name": product_name})
# #         if not product or product["quantity"] < quantity:
# #             raise HTTPException(status_code=400, detail="Product out of stock")

# #         new_quantity = product["quantity"] - quantity
# #         product_collection.update_one(
# #             {"name": product_name},
# #             {"$set": {"quantity": new_quantity}}
# #         )

# #         # Trigger dispensing
# #         if MotorController.dispense_product(product_name):
# #             # Record transaction
# #             transaction = {
# #                 "username": username,
# #                 "productName": product_name,
# #                 "quantity": quantity,
# #                 "amount": amount,
# #                 "transactionDate": time.strftime("%Y-%m-%d"),
# #                 "transactionTime": time.strftime("%H:%M:%S")
# #             }
# #             history_collection.insert_one(transaction)

# #             return {
# #                 "status": "success",
# #                 "message": f"Payment verified and {product_name} dispensed",
# #                 "new_balance": new_balance,
# #                 "transaction": transaction
# #             }
# #         else:
# #             # Rollback the payment if dispensing fails
# #             users_collection.update_one(
# #                 {"username": username},
# #                 {"$set": {"balance": user["balance"]}}
# #             )
# #             product_collection.update_one(
# #                 {"name": product_name},
# #                 {"$set": {"quantity": product["quantity"]}}
# #             )
# #             raise HTTPException(status_code=500, detail=f"Failed to dispense {product_name}")

# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail=str(e))

# # @app.post("/process_payment")
# # async def process_payment(request: PaymentRequest):
# #     payment_data = {
# #         "username": request.username,
# #         "amount": request.amount,
# #         "productName": request.productName,
# #         "quantity": request.quantity
# #     }
# #     return await verify_payment(payment_data)

# # @app.post("/save_transaction")
# # async def save_transaction(transaction: PurchaseRecord):
# #     try:
# #         transaction_data = {
# #             "username": transaction.username,
# #             "productName": transaction.productName,
# #             "quantity": transaction.quantity,
# #             "amount": transaction.amount,
# #             "transactionDate": transaction.transactionDate,
# #             "transactionTime": transaction.transactionTime,
# #         }

# #         result = history_collection.insert_one(transaction_data)
# #         if not result.inserted_id:
# #             raise HTTPException(status_code=500, detail="Failed to save transaction")

# #         return {"message": "Transaction saved successfully"}

# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail=str(e))

# # @app.get("/get_purchase_history")
# # async def get_purchase_history(username: str):
# #     transactions = list(history_collection.find({"username": username}).sort([("transactionDate", -1), ("transactionTime", -1)]))

# #     if not transactions:
# #         return {"message": "No transactions found"}

# #     return [
# #         {
# #             "productName": t.get("productName", "N/A"),
# #             "quantity": t.get("quantity", 0),
# #             "amount": t.get("amount", 0.0),
# #             "transactionDate": t.get("transactionDate", "N/A"),
# #             "transactionTime": t.get("transactionTime", "N/A"),
# #         }
# #         for t in transactions
# #     ]

# # @app.post("/load_balance")
# # async def load_balance(request: LoadBalanceRequest):
# #     username = request.username.strip().lower()
# #     user = get_user_by_username(username)

# #     if not user:
# #         raise HTTPException(status_code=404, detail="User not found")

# #     new_balance = user["balance"] + 20.00
# #     users_collection.update_one(
# #         {"username": username},
# #         {"$set": {"balance": new_balance}}
# #     )

# #     return {"message": f"Balance reloaded. New balance: {new_balance}"}






# # @app.get("/get_latest_transaction/{username}")
# # async def get_latest_transaction(username: str):
# #     try:
# #         # Find the most recent transaction for the user
# #         last_transaction = history_collection.find_one(
# #             {"username": username}, sort=[("transactionDate", -1), ("transactionTime", -1)]
# #         )

# #         if last_transaction:
# #             return {
# #                 "username": last_transaction["username"],
# #                 "productName": last_transaction["productName"],
# #                 "quantity": last_transaction["quantity"],
# #                 "amount": last_transaction["amount"],
# #                 "transactionDate": last_transaction["transactionDate"],
# #                 "transactionTime": last_transaction["transactionTime"],
# #                 "status": "success"
# #             }
# #         return {"status": "pending"}

# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail=str(e))


# # # Simulate Vending Machine Dispensing Product

# # @app.post("/dispense_product")
# # async def dispense_product(request: DispenseRequest):
# #     # Find the product
# #     product = product_collection.find_one({"productName": request.productName})
    
# #     if not product:
# #         raise HTTPException(status_code=404, detail="Product not found")
    
# #     if product["quantity"] < request.quantity:
# #         raise HTTPException(status_code=400, detail="Not enough stock available")
    
# #     # Update the quantity in the database
# #     new_quantity = product["quantity"] - request.quantity
# #     product_collection.update_one(
# #         {"productName": request.productName},
# #         {"$set": {"quantity": new_quantity}}
# #     )
    
# #     message = f"{request.quantity}x {request.productName} dispensed. New stock: {new_quantity}"
# #     print(message)  # Simulate hardware action

# #     return {"message": message, "new_quantity": new_quantity}


from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
from datetime import datetime
import uuid  # For generating unique transaction IDs

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
MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "vendme"
PRODUCT_COLLECTION_NAME = "productdetails"
USER_COLLECTION_NAME = "userdata"
HISTORY_COLLECTION_NAME = "purchase_history"

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
product_collection = db[PRODUCT_COLLECTION_NAME]
users_collection = db[USER_COLLECTION_NAME]
history_collection = db[HISTORY_COLLECTION_NAME]

# Pydantic Models
class PaymentRequest(BaseModel):
    username: str
    amount: float
    productName: str
    quantity: int

class PurchaseRecord(BaseModel):
    username: str
    productName: str
    quantity: int
    amount: float
    transactionID: str
    status: str  # "pending", "success", or "failed"
    transactionDate: str
    transactionTime: str

class ConfirmPaymentRequest(BaseModel):
    transactionID: str

# Helper function to fetch user by username
def get_user_by_username(username: str):
    return users_collection.find_one({"username": username.strip().lower()})

# Process Payment (Creates a Pending Transaction)
@app.post("/process_payment")
async def process_payment(request: PaymentRequest):
    username = request.username.strip().lower()
    user = get_user_by_username(username)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    current_balance = user.get("balance", 0.00)

    if current_balance < request.amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    # Generate unique transaction ID
    transaction_id = str(uuid.uuid4())

    # Save transaction as "pending"
    transaction_data = {
        "username": username,
        "productName": request.productName,
        "quantity": request.quantity,
        "amount": request.amount,
        "transactionID": transaction_id,
        "status": "pending",
        "transactionDate": datetime.now().strftime("%Y-%m-%d"),
        "transactionTime": datetime.now().strftime("%H:%M:%S"),
    }
    history_collection.insert_one(transaction_data)

    return {"message": "Payment initiated", "transactionID": transaction_id, "status": "pending"}

# Confirm Payment (Updates Transaction Status to "Success")
@app.post("/confirm_payment")
async def confirm_payment(request: ConfirmPaymentRequest):
    transaction = history_collection.find_one({"transactionID": request.transactionID})

    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    if transaction["status"] == "success":
        return {"message": "Payment already confirmed"}

    # Mark payment as successful
    history_collection.update_one(
        {"transactionID": request.transactionID},
        {"$set": {"status": "success"}}
    )

    # Deduct balance from user
    username = transaction["username"]
    amount = transaction["amount"]
    users_collection.update_one(
        {"username": username},
        {"$inc": {"balance": -amount}}
    )

    return {"message": "Payment confirmed successfully", "status": "success"}

# Check Payment Status
@app.get("/check_payment_status")
async def check_payment_status(username: str):
    transaction = history_collection.find_one(
        {"username": username},
        sort=[("transactionDate", -1), ("transactionTime", -1)]  # Get latest transaction
    )

    if not transaction:
        raise HTTPException(status_code=404, detail="No transactions found")

    return {
        "transactionID": transaction["transactionID"],
        "status": transaction["status"],
        "product": transaction["productName"],
        "amount": transaction["amount"]
    }

# Fetch User Balance
@app.get("/get_balance")
async def get_balance(username: str):
    username = username.strip().lower()
    user = get_user_by_username(username)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {"balance": user.get("balance", 0.00)}

# Get Purchase History
@app.get("/get_purchase_history")
async def get_purchase_history(username: str):
    transactions = list(history_collection.find({"username": username}).sort([("transactionDate", -1), ("transactionTime", -1)]))

    if not transactions:
        return {"message": "No transactions found"}

    return [
        {
            "transactionID": t.get("transactionID"),
            "productName": t.get("productName", "N/A"),
            "quantity": t.get("quantity", 0),
            "amount": t.get("amount", 0.0),
            "status": t.get("status"),
            "transactionDate": t.get("transactionDate", "N/A"),
            "transactionTime": t.get("transactionTime", "N/A"),
        }
        for t in transactions
    ]

# Load Balance (For Testing)
@app.post("/load_balance")
async def load_balance(username: str):
    user = get_user_by_username(username)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Add a fixed amount for testing
    new_balance = user["balance"] + 50.00
    users_collection.update_one(
        {"username": username},
        {"$set": {"balance": new_balance}}
    )

    return {"message": f"Balance updated. New balance: {new_balance}", "new_balance": new_balance}

# Print API URL on Startup
@app.on_event("startup")
async def on_startup():
    print("API is running! Access it at http://localhost:8000")
