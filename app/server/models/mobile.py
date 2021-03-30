from typing import Optional

from pydantic import BaseModel, Field

class MobileSchema(BaseModel):
    model: str = Field(..., description="Model name", max_length=300)
    company: str = Field(..., description="Company name", max_length=400)
    price: int = Field(None, description="price", gt=10)

    class Config:
        schema_extra = {
            "example": {
                "model": "galaxy",
                "company": "samsung",
                "price": 200000
            }
        }

class UpdateMobileSchema(BaseModel):
    model: Optional[str] 
    company: Optional[str]
    price: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "model": "galaxyS21",
                "company": "samsung",
                "price": 200000
            }
        }


def ResponseModel(data, message):
    return{
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponse(error, code, message):
    return {"error":error, "code":code, "messge":message}