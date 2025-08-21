from app.DAL_MONGO import DAL_mongo
import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def start():




    return dal.get_all()

