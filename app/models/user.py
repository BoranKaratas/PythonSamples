from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['bokaDB']

class User:
    collection = db['users']

    @classmethod
    def create(cls, user_data):
        return cls.collection.insert_one(user_data)

    @classmethod
    def find_by_email(cls, email):
        return cls.collection.find_one({'email': email})