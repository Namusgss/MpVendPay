# # # from fastapi import FastAPI
# # # from fastapi.middleware.cors import CORSMiddleware
# # # from motor.motor_asyncio import AsyncIOMotorClient
# # # import socket

# # # # Initialize FastAPI
# # # app = FastAPI()

# # # # Enable CORS
# # # app.add_middleware(
# # # CORSMiddleware,
# # # allow_origins=["*"], # Allow all origins for simplicity; restrict in production
# # # allow_credentials=True,
# # # allow_methods=["*"],
# # # allow_headers=["*"],
# # # )

# # # MONGO_URI = "mongodb://localhost:27017" # Replace with your MongoDB URI
# # # DATABASE_NAME = "vendme"
# # # COLLECTION_NAME = "productdetails"

# # # client = AsyncIOMotorClient(MONGO_URI)
# # # db = client[DATABASE_NAME]
# # # collection = db[COLLECTION_NAME]

# # # # Helper to serialize MongoDB documents
# # # def serialize_doc(doc):
# # #     return {
# # # "id": str(doc["_id"]), # Convert ObjectId to string
# # # "name": doc.get("name", ""), # Use .get() to avoid KeyError
# # # "price": doc.get("price", 0.0),
# # # "quantity": doc.get("quantity", 0),
# # # "image": doc.get("image", ""),
# # # }

# # # # Route to fetch all items
# # # @app.get("/items")
# # # async def get_items():
# # #     docs = await collection.find().to_list(100) # Fetch up to 100 documents
# # #     return [serialize_doc(doc) for doc in docs]

# # # # Root endpoint for testing
# # # @app.get("/")
# # # async def root():
# # #     return {"message": "FastAPI with MongoDB is running!"}

# # # # Print the actual IP and accessible address on startup
# # # @app.on_event("startup")
# # # async def on_startup():
# # #     hostname = socket.gethostname()
# # #     local_ip = socket.gethostbyname(hostname)
# # #     print(f"API is running! Access it at http://{local_ip}:8000")

# # # from fastapi import FastAPI
# # # from fastapi.middleware.cors import CORSMiddleware
# # # from motor.motor_asyncio import AsyncIOMotorClient

# # # # Initialize FastAPI
# # # app = FastAPI()

# # # # Add CORS middleware
# # # app.add_middleware(
# # #     CORSMiddleware,
# # #     allow_origins=["*"],  # You can specify your Expo Go device's IP here instead of "*"
# # #     allow_methods=["*"],
# # #     allow_headers=["*"],
# # # )

# # # MONGO_URI = "mongodb://localhost:27017"  # Replace with your MongoDB URI
# # # DATABASE_NAME = "vendme"
# # # COLLECTION_NAME = "productdetails"

# # # client = AsyncIOMotorClient(MONGO_URI)
# # # db = client[DATABASE_NAME]
# # # collection = db[COLLECTION_NAME]

# # # # Helper to serialize MongoDB documents
# # # def serialize_doc(doc):
# # #     return {
# # #         "id": str(doc["_id"]),  # Convert ObjectId to string
# # #         "name": doc.get("name", ""),  # Use .get() to avoid KeyError
# # #         "price": doc.get("price", 0.0),
# # #         "quantity": doc.get("quantity", 0),
# # #         "image": doc.get("image", ""),
# # #     }

# # # # Route to fetch all items
# # # @app.get("/items")
# # # async def get_items():
# # #     docs = await collection.find().to_list(100)  # Fetch up to 100 documents
# # #     return [serialize_doc(doc) for doc in docs]

# # # # Root endpoint for testing
# # # @app.get("/")
# # # async def root():
# # #     return {"message": "FastAPI with MongoDB is running!"}




# # # from fastapi import FastAPI, HTTPException, Body
# # # from fastapi.middleware.cors import CORSMiddleware
# # # from motor.motor_asyncio import AsyncIOMotorClient
# # # import bcrypt
# # # from pydantic import BaseModel, EmailStr
# # # import socket

# # # # Initialize FastAPI
# # # app = FastAPI()

# # # # Enable CORS
# # # app.add_middleware(
# # #     CORSMiddleware,
# # #     allow_origins=["*"],  # Allow all origins for simplicity; restrict in production
# # #     allow_credentials=True,
# # #     allow_methods=["*"],
# # #     allow_headers=["*"],
# # # )

# # # # MongoDB URI and collection names
# # # MONGO_URI = "mongodb://localhost:27017"  # Replace with your MongoDB URI
# # # DATABASE_NAME = "vendme"
# # # PRODUCT_COLLECTION_NAME = "productdetails"  # Collection for product details
# # # USER_COLLECTION_NAME = "userdata"  # Collection for user data

# # # client = AsyncIOMotorClient(MONGO_URI)
# # # db = client[DATABASE_NAME]
# # # product_collection = db[PRODUCT_COLLECTION_NAME]
# # # user_collection = db[USER_COLLECTION_NAME]

# # # # Define the Pydantic models for user data
# # # class User(BaseModel):
# # #     username: str
# # #     password: str
# # #     email: EmailStr  # Email validation
# # #     number: str

# # # # Helper to serialize MongoDB documents for products
# # # def serialize_product_doc(doc):
# # #     return {
# # #         "id": str(doc["_id"]),  # Convert ObjectId to string
# # #         "name": doc.get("name", ""),
# # #         "price": doc.get("price", 0.0),
# # #         "quantity": doc.get("quantity", 0),
# # #         "image": doc.get("image", ""),
# # #     }

# # # # Helper to serialize MongoDB documents for users (for testing purposes)
# # # def serialize_user_doc(doc):
# # #     return {
# # #         "id": str(doc["_id"]),
# # #         "username": doc.get("username", ""),
# # #         "email": doc.get("email", ""),
# # #         "number": doc.get("number", ""),
# # #     }

# # # # Route to fetch all product items
# # # @app.get("/items")
# # # async def get_items():
# # #     docs = await product_collection.find().to_list(100)  # Fetch up to 100 products
# # #     return [serialize_product_doc(doc) for doc in docs]

# # # # Route to register a new user
# # # @app.post("/register")
# # # async def register(user: User):
# # #     # Hash the password before saving it
# # #     hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    
# # #     # Check if the user already exists
# # #     existing_user = await user_collection.find_one({"username": user.username})
# # #     if existing_user:
# # #         raise HTTPException(status_code=400, detail="Username already exists")

# # #     # Save the new user to the database
# # #     new_user = {
# # #         "username": user.username,
# # #         "password": hashed_password,
# # #         "email": user.email,
# # #         "number": user.number,
# # #     }
# # #     result = await user_collection.insert_one(new_user)
# # #     return {"message": "User registered successfully", "id": str(result.inserted_id)}

# # # # Route to login
# # # @app.post("/login")
# # # async def login(user: User):
# # #     # Retrieve the user from the database
# # #     existing_user = await user_collection.find_one({"username": user.username})
# # #     if not existing_user:
# # #         raise HTTPException(status_code=400, detail="Invalid credentials")
    
# # #     # Compare the provided password with the stored hashed password
# # #     if not bcrypt.checkpw(user.password.encode('utf-8'), existing_user["password"]):
# # #         raise HTTPException(status_code=400, detail="Invalid credentials")
    
# # #     return {"message": "Login successful", "user": serialize_user_doc(existing_user)}

# # # # Route to fetch all users (for testing purposes)
# # # @app.get("/users")
# # # async def get_users():
# # #     docs = await user_collection.find().to_list(100)
# # #     return [serialize_user_doc(doc) for doc in docs]

# # # # Root endpoint for testing
# # # @app.get("/")
# # # async def root():
# # #     return {"message": "FastAPI with MongoDB is running!"}

# # # # Print the actual IP and accessible address on startup
# # # @app.on_event("startup")
# # # async def on_startup():
# # #     hostname = socket.gethostname()
# # #     local_ip = socket.gethostbyname(hostname)
# # #     print(f"API is running! Access it at http://{local_ip}:8000")

# # # newww

# # from fastapi import FastAPI, HTTPException, Body
# # from fastapi.middleware.cors import CORSMiddleware
# # from motor.motor_asyncio import AsyncIOMotorClient
# # import bcrypt
# # from pydantic import BaseModel, EmailStr
# # import socket
# # from datetime import datetime, timedelta
# # from jose import JWTError, jwt

# # # Initialize FastAPI
# # app = FastAPI()

# # # Enable CORS
# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["*"],  # Allow all origins for simplicity; restrict in production
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# # # MongoDB URI and collection names
# # MONGO_URI = "mongodb://localhost:27017"  # Replace with your MongoDB URI
# # DATABASE_NAME = "vendme"
# # PRODUCT_COLLECTION_NAME = "productdetails"  # Collection for product details
# # USER_COLLECTION_NAME = "userdata"  # Collection for user data

# # client = AsyncIOMotorClient(MONGO_URI)
# # db = client[DATABASE_NAME]
# # product_collection = db[PRODUCT_COLLECTION_NAME]
# # user_collection = db[USER_COLLECTION_NAME]

# # # JWT Secret and Algorithm (for token generation)
# # SECRET_KEY = "your_secret_key"  # Change to a secure secret
# # ALGORITHM = "HS256"
# # ACCESS_TOKEN_EXPIRE_MINUTES = 30

# # # Define the Pydantic models for user data
# # class User(BaseModel):
# #     username: str
# #     password: str
# #     email: EmailStr  # Email validation
# #     number: str

# # # Helper to serialize MongoDB documents for users (for testing purposes)
# # def serialize_user_doc(doc):
# #     return {
# #         "id": str(doc["_id"]),
# #         "username": doc.get("username", ""),
# #         "email": doc.get("email", ""),
# #         "number": doc.get("number", ""),
# #     }

# # # JWT Token Generation Helper
# # def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
# #     to_encode = data.copy()
# #     expire = datetime.utcnow() + expires_delta
# #     to_encode.update({"exp": expire})
# #     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
# #     return encoded_jwt

# # # Route to fetch all product items
# # @app.get("/items")
# # async def get_items():
# #     docs = await product_collection.find().to_list(100)  # Fetch up to 100 products
# #     return [serialize_product_doc(doc) for doc in docs]

# # # Route to register a new user
# # @app.post("/register")
# # async def register(user: User):
# #     # Hash the password before saving it
# #     hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    
# #     # Check if the user already exists
# #     existing_user = await user_collection.find_one({"username": user.username})
# #     if existing_user:
# #         raise HTTPException(status_code=400, detail="Username already exists")

# #     # Save the new user to the database
# #     new_user = {
# #         "username": user.username,
# #         "password": hashed_password,
# #         "email": user.email,
# #         "number": user.number,
# #     }
# #     result = await user_collection.insert_one(new_user)
# #     return {"message": "User registered successfully", "id": str(result.inserted_id)}

# # # Route to login and return a JWT token
# # @app.post("/login")
# # async def login(user: User):
# #     # Retrieve the user from the database
# #     existing_user = await user_collection.find_one({"username": user.username})
# #     if not existing_user:
# #         raise HTTPException(status_code=400, detail="Invalid credentials")
    
# #     # Compare the provided password with the stored hashed password
# #     if not bcrypt.checkpw(user.password.encode('utf-8'), existing_user["password"]):
# #         raise HTTPException(status_code=400, detail="Invalid credentials")
    
# #     # Create a JWT token
# #     access_token = create_access_token(
# #         data={"sub": user.username}
# #     )
    
# #     return {"message": "Login successful", "access_token": access_token, "token_type": "bearer"}

# # # Route to fetch all users (for testing purposes)
# # @app.get("/users")
# # async def get_users():
# #     docs = await user_collection.find().to_list(100)
# #     return [serialize_user_doc(doc) for doc in docs]

# # # Root endpoint for testing
# # @app.get("/")
# # async def root():
# #     return {"message": "FastAPI with MongoDB is running!"}

# # # Print the actual IP and accessible address on startup
# # @app.on_event("startup")
# # async def on_startup():
# #     hostname = socket.gethostname()
# #     local_ip = socket.gethostbyname(hostname)
# #     print(f"API is running! Access it at http://{local_ip}:8000")



# from fastapi import FastAPI, HTTPException, Body
# from fastapi.middleware.cors import CORSMiddleware
# from motor.motor_asyncio import AsyncIOMotorClient
# import bcrypt
# from pydantic import BaseModel, EmailStr
# import socket
# from datetime import datetime, timedelta
# from jose import JWTError, jwt
# from typing import List, Optional

# # Initialize FastAPI
# app = FastAPI()

# # Enable CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allow all origins for simplicity; restrict in production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # MongoDB URI and collection names
# MONGO_URI = "mongodb://localhost:27017"  # Replace with your MongoDB URI
# DATABASE_NAME = "vendme"
# PRODUCT_COLLECTION_NAME = "productdetails"  # Collection for product details
# USER_COLLECTION_NAME = "userdata"  # Collection for user data

# client = AsyncIOMotorClient(MONGO_URI)
# db = client[DATABASE_NAME]
# product_collection = db[PRODUCT_COLLECTION_NAME]
# user_collection = db[USER_COLLECTION_NAME]

# # JWT Secret and Algorithm (for token generation)
# SECRET_KEY = "your_secret_key"  # Change to a secure secret
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# # Define the Pydantic models for user data
# class User(BaseModel):
#     username: str
#     password: str
#     email: EmailStr  # Email validation
#     number: str

# class Product(BaseModel):
#     name: str
#     price: float
#     quantity: int
#     description: Optional[str] = None  # Optional description field
#     image_url: Optional[str] = None  # Optional image URL field

# # Helper to serialize MongoDB documents for products
# def serialize_product_doc(doc):
#     return {
#         "id": str(doc["_id"]),
#         "name": doc.get("name", ""),
#         "price": doc.get("price", 0),
#         "quantity": doc.get("quantity", 0),
#         "description": doc.get("description", ""),
#         "image_url": doc.get("image_url", ""),
#     }

# # Helper to serialize MongoDB documents for users (for testing purposes)
# def serialize_user_doc(doc):
#     return {
#         "id": str(doc["_id"]),
#         "username": doc.get("username", ""),
#         "email": doc.get("email", ""),
#         "number": doc.get("number", ""),
#     }

# # JWT Token Generation Helper
# def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + expires_delta
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt

# # Route to fetch all product items
# @app.get("/items", response_model=List[Product])
# async def get_items():
#     docs = await product_collection.find().to_list(100)  # Fetch up to 100 products
#     return [serialize_product_doc(doc) for doc in docs]

# # Route to register a new user
# @app.post("/register")
# async def register(user: User):
#     # Hash the password before saving it
#     hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    
#     # Check if the user already exists
#     existing_user = await user_collection.find_one({"username": user.username})
#     if existing_user:
#         raise HTTPException(status_code=400, detail="Username already exists")

#     # Save the new user to the database
#     new_user = {
#         "username": user.username,
#         "password": hashed_password,
#         "email": user.email,
#         "number": user.number,
#     }
#     result = await user_collection.insert_one(new_user)
#     return {"message": "User registered successfully", "id": str(result.inserted_id)}

# # Route to login and return a JWT token
# @app.post("/login")
# async def login(user: User):
#     # Retrieve the user from the database
#     existing_user = await user_collection.find_one({"username": user.username})
#     if not existing_user:
#         raise HTTPException(status_code=400, detail="Invalid credentials")
    
#     # Compare the provided password with the stored hashed password
#     if not bcrypt.checkpw(user.password.encode('utf-8'), existing_user["password"]):
#         raise HTTPException(status_code=400, detail="Invalid credentials")
    
#     # Create a JWT token
#     access_token = create_access_token(
#         data={"sub": user.username}
#     )
    
#     return {"message": "Login successful", "access_token": access_token, "token_type": "bearer"}

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


from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import bcrypt
from pydantic import BaseModel, EmailStr
import socket
from datetime import datetime, timedelta
from jose import JWTError, jwt

# Initialize FastAPI
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for simplicity; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB URI and collection names
MONGO_URI = "mongodb://localhost:27017"  # Replace with your MongoDB URI
DATABASE_NAME = "vendme"
PRODUCT_COLLECTION_NAME = "productdetails"  # Collection for product details
USER_COLLECTION_NAME = "userdata"  # Collection for user data

client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]
product_collection = db[PRODUCT_COLLECTION_NAME]
user_collection = db[USER_COLLECTION_NAME]

# JWT Secret and Algorithm (for token generation)
SECRET_KEY = "your_secret_key"  # Change to a secure secret
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Define the Pydantic models for user data
class User(BaseModel):
    username: str
    password: str
    email: EmailStr  # Email validation
    number: str

# Helper to serialize MongoDB documents for users (for testing purposes)
def serialize_user_doc(doc):
    return {
        "id": str(doc["_id"]),
        "username": doc.get("username", ""),
        "email": doc.get("email", ""),
        "number": doc.get("number", ""),
    }

# JWT Token Generation Helper
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Route to fetch all product items
@app.get("/items")
async def get_items():
    docs = await product_collection.find().to_list(100)  # Fetch up to 100 products
    return [serialize_user_doc(doc) for doc in docs]

# Route to register a new user
@app.post("/register")
async def register(user: User):
    # Hash the password before saving it
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    
    # Check if the user already exists
    existing_user = await user_collection.find_one({"username": user.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Save the new user to the database
    new_user = {
        "username": user.username,
        "password": hashed_password,
        "email": user.email,
        "number": user.number,
    }
    result = await user_collection.insert_one(new_user)
    return {"message": "User registered successfully", "id": str(result.inserted_id)}

# Route to login and return a JWT token
@app.post("/login")
async def login(user: User):
    print(user)
    print(f"Received login request with username: {user.username}")
 
    # Retrieve the user from the database
    existing_user = await user_collection.find_one({"username": user.username})
    if not existing_user:
        print(f"User {user.username} not found.")
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    # Debug: print the stored hashed password
    print(f"Stored password hash: {existing_user['password']}")
    
    # Compare the provided password with the stored hashed password
    if not bcrypt.checkpw(user.password.encode('utf-8'), existing_user["password"].encode('utf-8')):
        print(f"Password mismatch for user {user.username}")
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"message": "Login successful", "access_token": access_token, "token_type": "bearer"}

# Route to fetch all users (for testing purposes)
@app.get("/users")
async def get_users():
    docs = await user_collection.find().to_list(100)
    return [serialize_user_doc(doc) for doc in docs]

# Root endpoint for testing
@app.get("/")
async def root():
    return {"message": "FastAPI with MongoDB is running!"}

# Print the actual IP and accessible address on startup
@app.on_event("startup")
async def on_startup():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"API is running! Access it at http://{local_ip}:8000")
