from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class HouseBase(BaseModel):
    owner_id: int = Field(...)
    name: str = Field(..., min_length=5, max_length=50)
    address: str = Field(..., max_length=150)
    
class HouseCreate(HouseBase):
    pass

class HouseUpdate(BaseModel):
    owner_id: Optional[int] = Field(None)
    name: Optional[str] = Field(None, min_length=5, max_length=50)
    address: Optional[str] = Field(None, max_length=150)

class HouseResponse(HouseBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True) 