from fastapi import FastAPI
from app.manager import Manager
import json

app = FastAPI()

m = Manager()

@app.get("/")
def start():
    m.clean_and_order()

    data = m.df.head(100).to_json(orient="records")
    parsed = json.loads(data)

    return parsed

