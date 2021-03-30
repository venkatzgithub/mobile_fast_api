import uvicorn

if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)

"""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

# temp database
mobiledb = "mongodb://localhost:27017/mobile_DB"

# Mobile model to store Mobiles
class Mobile(BaseModel):
    id: int
    name: str
    price: float

# Home/welcome route
@app.get("/")
def read_root():
    return {"greetings": "Welcome to Mobilestore!!!"}

# Get all Mobiles
@app.get("/mobiles")
def get_mobiles():
    return mobiledb

# get single mobile
@app.get("/mobiles/{mobile_id}")
def get_a_mobile(mobile_id: int):
    mobile = mobile_id - 1
    return mobiledb[mobile]

# add a new mobile
@app.post("/mobiles")
def add_mobile(mobile: mobile):
    mobiledb.append(mobile.dict())
    return mobiledb[-1]

# delete a mobile
@app.delete("/mobiles/{mobile_id}")
def delete_mobile(mobile_id: int):
    mobiledb.pop(mobile_id-1)
    return {"task": "deletion successful"}
"""