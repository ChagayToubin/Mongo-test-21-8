from pymongo import MongoClient
from pandas import pandas as pd


class DAL_mongo:

    def __init__(self, host, database, collection, user, password):
        self.host = host
        self.database = database
        self.collection = collection
        self.user = user
        self.password = password
        self.URI = self.get_URI()

        self.client = None
        self.data=None

    def get_URI(self):
        if self.user and self.password:
            URI = f"mongodb+srv://{self.user}:{self.password}@{self.host}/"
        else:
            URI = f"mongodb://{self.host}:27017"
        return URI

    def open_connection(self):
        try:
            self.client = MongoClient(self.URI)
            return True
        except Exception as e:
            print("Error: ", e)
            return False
    def get_all(self):

        self.open_connection()
        db = self.client[self.database]
        collection = db[self.collection]
        data = collection.find({}, {"_id": 0})
        self.data= data
        return pd.DataFrame((self.data))



    def close_connection(self):
        if self.client:
            self.client.close()