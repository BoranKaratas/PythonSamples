from pymongo import MongoClient
from app.config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client['bokaDB']

class User:
    collection = db['users']

    @classmethod
    def create(cls, user_data):
        return cls.collection.insert_one(user_data)

    @classmethod
    def find_by_email(cls, email):
        return cls.collection.find_one({'email': email})