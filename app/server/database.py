import motor.motor_asyncio
from bson.objectid import ObjectId

DATABASE_URL = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)

database = client.mobile_DB

mobile_collection =  database.get_collection("mobile_collection")

# helpers

def mobile_helper(mobile) -> dict:
    return {
        "id": str(mobile["_id"]),
        "model": mobile["model"],
        "company": mobile["company"],
        "price": str(mobile["price"])
    }

# Retrieve all the mobiles present in the database
async def retrieve_mobiles():
    mobiles = []
    async for mobile in mobile_collection.find():
        mobiles.append(mobile_helper(mobile))
    return mobiles

# Add a mobile into the database
async def add_mobile(mobile_data: dict) -> dict:
    mobile = await mobile_collection.insert_one(mobile_data)
    new_mobile = await mobile_collection.find_one({"_id": mobile.inserted_id})
    return mobile_helper(new_mobile)

# Retrieve a mobile by id
async def retrieve_mobile(id: str) -> dict:
    mobile = await mobile_collection.find_one({"_id": ObjectId(id)})
    if mobile:
        return mobile_helper(mobile)

# Update a mobile by id
async def update_mobile(id: str, mobile_data: dict) -> dict:
    if len(mobile_data)<1:
        return False
    mobile = await mobile_collection.find_one({"_id":ObjectId(id)})
    if mobile:
        updated_mobile = await mobile_collection.update_one(
            {"_id":ObjectId(id)}, {"$set":mobile_data}
        )
        if updated_mobile:
            return True
    return False

# Delete a mobile by id
async def delete_mobile(id: str):
    mobile = await mobile_collection.find_one({"_id": ObjectId(id)})
    if mobile:
        await mobile_collection.delete_one({"_id": ObjectId(id)})
        return True
