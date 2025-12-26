import os
import certifi
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB connection string from environment variable
uri = os.getenv('MONGODB_URL')

if not uri:
    raise ValueError("MONGODB_URL not found in environment variables")

# MongoDB Client Configuration
# Using certifi for SSL/TLS certificates and allowing invalid certificates 
# to ensure compatibility with Render's environment
client = MongoClient(
    uri,
    tls=True,
    tlsCAFile=certifi.where(),
    tlsAllowInvalidCertificates=True,
    server_api=ServerApi('1')
)

# Database and Collection configuration with fallbacks
db_name = os.getenv("MONGODB_DB", "python_fastapi")
collection_name = os.getenv("MONGODB_COLLECTION", "films")

db = client[db_name]
collection = db[collection_name]

def ping_db():
    try:
        client.admin.command('ping')
        print(f"Successfully connected to MongoDB: {db_name} -> {collection_name}")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")


ping_db()