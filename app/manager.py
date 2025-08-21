from app.DAL_MONGO import DAL_mongo
from app.processor import Processor as p
# from DAL_MONGO import DAL_mongo
# from processor import Processor as p
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
       self.df=p.Pweapon_find(self.df)

    def MEmotions_of_text(self):
        self.df=p.PEmotions_of_text(self.df)

    def clean_and_order(self):
        self.MFinding_the_rarest_word()
        self.Mweapon_find()
        self.MEmotions_of_text()



