# backend/database.py

from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))

db = client["career_saas"]
analyses = db["analyses"]

def save_analysis(user_id, data):
    data["user_id"] = user_id
    analyses.insert_one(data)

def get_user_history(user_id):
    return list(analyses.find({"user_id": user_id}, {"_id": 0}))
