  
from fastapi import FastAPI

from app.server.resources.mobile import router as MobileRouter

app = FastAPI()

app.include_router(MobileRouter, tags=["Mobile"], prefix="/mobile")

@app.get("/", tags=["Home"])
async def hello_world():
    return {"message":"welcome!!!"}