from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.test

cursor = db.review1.find()
for document in cursor:
    print(document)
