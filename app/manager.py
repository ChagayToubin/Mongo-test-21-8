from app.DAL_MONGO import DAL_mongo
import os
HOST = os.getenv("HOST", "iranmaldb.gurutam.mongodb.net")
USER = os.getenv("USER","IRGC" )
PASSWORD = os.getenv("PASSWORD","iraniraniran" )
DB = os.getenv("DATABASE", "IranMalDB")
COLLECTION = os.getenv("COLLECTION", "tweets")

class Manager:
    def __init__(self):
        self.dal_mongo=DAL_mongo(HOST, DB, COLLECTION, USER, PASSWORD)
    def MFinding_the_rarest_word(self):
        data=self.dal_mongo.get_all()



