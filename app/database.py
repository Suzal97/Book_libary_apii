# app/database.py
from pymongo import MongoClient
from app.core.config import settings

# Initialize the MongoDB client and database
client = MongoClient(settings.MONGO_URL)
db = client[settings.DATABASE_NAME]

# Function to get the books collection
def get_book_collection():
    return db["books"]

