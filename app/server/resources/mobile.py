from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    retrieve_mobiles,
    add_mobile,
    retrieve_mobile,
    update_mobile,
    delete_mobile
)

from app.server.models.mobile import (
    MobileSchema,
    UpdateMobileSchema,
    ResponseModel,
    ErrorResponse
)

router = APIRouter()

@router.post("/", response_description="Mobile data added into the database")
async def add_mobile_data(mobile: MobileSchema = Body(...)):
    mobile = jsonable_encoder(mobile)
    new_mobile = await add_mobile(mobile)
    return ResponseModel(new_mobile, "Mobile added successfully.")

@router.get("/", response_description="Mobiles retrieved")
async def get_mobiles():
    mobiles = await retrieve_mobiles()
    if mobiles:
        return ResponseModel(mobiles, "Mobiles retrieved successfully")
    return ResponseModel(mobiles, "Empty list returned")

@router.get("/{id}", response_description="Mobile retrieved successfully")
async def get_mobile(id: str):
    mobile = await retrieve_mobile(id)
    if mobile:
        return ResponseModel(mobile, "Mobile retrieved successfully")
    return ErrorResponse("An error occured", 404, "Mobile dosen't exist")

@router.put("/{id}", response_description="Mobile updated successfully")
async def update_mobile_data(id: str, mobile: UpdateMobileSchema = Body(...)):
    mobile = {k:v for k,v in mobile.dict().items() if v is not None}
    updated_mobile = await update_mobile(id, mobile)
    if updated_mobile:
        return ResponseModel(
            f"Mobile with the id {id} updated successfully",
            "mobile updated successfully"
        )
    return ErrorResponse(
        "An error occured",
        404,
        "There was an error updating the mobile data"
    )

@router.delete("/{id}", response_description="Mobile deleted successfully")
async def delete_mobile_data(id: str):
    mobile = await delete_mobile(id)
    if mobile:
        return ResponseModel(
            f"Mobile data with id {id} deleted successfully",
            "Mobile data deleted successfully" 
        )
    return ErrorResponse(
        "An error occured",
        404,
        f"Mobile data with id {id} does not exist"
    )

