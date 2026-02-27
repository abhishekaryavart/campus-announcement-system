from pymongo import MongoClient
import config

def get_db():
    client = MongoClient(config.MONGO_URI)
    db = client.campus_announcement_db
    return db
