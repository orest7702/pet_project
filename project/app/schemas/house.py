from pydantic import BaseModel, Field
from typing import Optional

class HouseBase(BaseModel):
    name: str = Field(None, min_length=5, max_length=50)
    address: str = Field(..., max_length=150)
    
class HouseCreate(HouseBase):
    pass

class HouseUpdate(HouseBase):
    name: Optional[str] = Field(None, min_length=5, max_length=50)
    address: Optional[str] = Field(None, max_length=150)

class HouseResponse(HouseBase):
    id: int

    class Config:
        from_attributes = True