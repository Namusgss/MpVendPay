from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from pymongo import MongoClient

# Initialize FastAPI app
app = FastAPI()

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "venddatabase"
COLLECTION_NAME = "mycollection"

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
users_collection = db[COLLECTION_NAME]

# Pydantic Models
class UserCreate(BaseModel):
    username: str
    password: str  # Store passwords as plaintext
    email: EmailStr
    number: str

class UserLogin(BaseModel):
    username: str
    password: str

# Function to check if user exists
def get_user_by_username(username: str):
    return users_collection.find_one({"username": username})

def get_user_by_email(email: str):
    return users_collection.find_one({"email": email})

# Register User Endpoint
@app.post("/register")
async def register_user(user: UserCreate):
    if get_user_by_email(user.email):
        raise HTTPException(status_code=400, detail="Email already registered.")
    if get_user_by_username(user.username):
        raise HTTPException(status_code=400, detail="Username already taken.")

    # Insert user into database (storing password as plaintext)
    user_data = {
        "username": user.username,
        "email": user.email,
        "password": user.password,  # Storing as plaintext
        "number": user.number
    }
    users_collection.insert_one(user_data)

    return {"message": "User registered successfully"}

# Login User Endpoint
@app.post("/login")
async def login_user(user: UserLogin):
    db_user = get_user_by_username(user.username)

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid username")
    
    if user.password != db_user["password"]:
        raise HTTPException(status_code=400, detail="Invalid password")

    return {"message": "Login successful"}
