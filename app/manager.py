from app.DAL_MONGO import DAL_mongo
from app.processor import Processor as p
import os
HOST = os.getenv("HOST", "iranmaldb.gurutam.mongodb.net")
USER = os.getenv("USER","IRGC" )
PASSWORD = os.getenv("PASSWORD","iraniraniran" )
DB = os.getenv("DATABASE", "IranMalDB")
COLLECTION = os.getenv("COLLECTION", "tweets")

class Manager:
    def __init__(self):
        self.dal_mongo=DAL_mongo(HOST, DB, COLLECTION, USER, PASSWORD)
        self.df=self.dal_mongo.get_all()
    def MFinding_the_rarest_word(self):
        self.df= p.PFinding_the_rarest_word(self.df)
    def Mweapon_find(self):
       self.df= self.df=p.Pweapon_find(self.df)


m=Manager()
m.MFinding_the_rarest_word()
m.Mweapon_find()

print(m.df[["weapons_detected","rarest_word"]].head(100))


