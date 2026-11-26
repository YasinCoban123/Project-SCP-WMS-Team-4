import os
import certifi

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

client = MongoClient(
    os.environ["MONGODB_URI"],
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=5000
)

database = client[os.environ["MONGODB_DB"]]

products_collection = database["products"]
orders_collection = database["orders"]


if __name__ == "__main__":
    client.admin.command("ping")
    print("Connected successfully")
    client.close()