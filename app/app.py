from fastapi import FastAPI
from app.manager import Manager

app = FastAPI()

m=Manager()
m.MFinding_the_rarest_word()
m.Mweapon_find()

@app.get("/")
def start():
    return m.df.to_json('temp.json.gz', orient='records', lines=True, compression='gzip')


