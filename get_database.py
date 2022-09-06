from pymongo import MongoClient
import os

user = os.environ['MONGO_USER']
password = os.environ['MONGO_PASS']
client = MongoClient(
    'mongodb://mongodb:27017/?authSource=admin&readPreference=secondary&directConnection=true&ssl=false',
    username=user,
    password=password)
database = client.fastapi

