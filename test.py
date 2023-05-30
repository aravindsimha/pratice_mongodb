from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

password = "Rameswararao@1"
encoded_password = quote_plus(password)

uri = f"mongodb+srv://aravindsimha:{encoded_password}@datascience.kakeuwt.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


data = {
    "name" : "network",
    "email" : "network@gmail.com",
    "surname" : "mobile"
}


# from line 21 to 25 we create a just distionary

database = client['jio']
#here we are giving client name as jio
collection = database['details']
# adding another subset in jio
collection.insert_one(data)
#inserting only one at a time




""" WE CAN PUSH ALL THIS CODE INTO GITHUB AT A TIME BY SELECTING THE VSC AND IN THAT SELECT CREATE GIT REPOSITORY"""
# AS WE download git download then we can use this repository
