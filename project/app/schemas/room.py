from pydantic import BaseModel, Field
from typing import Optional

class RoomBase(BaseModel):
    name: str = Field(None, min_length=5, max_length=50)
    
class RoomCreate(RoomBase):
    pass

class RoomUpdate(RoomBase):
    name: Optional[str] = Field(None, min_length=5, max_length=50)

class RoomResponse(RoomBase):
    id: int

    class Config:
        from_attributes = True
        