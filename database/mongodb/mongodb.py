from pymongo import MongoClient
from config import config


# Connect with the portnumber and host
client = MongoClient(config.mongoclient)
