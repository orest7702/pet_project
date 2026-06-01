from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class RoomBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=50)
    house_id: int = Field(...)

class RoomCreate(RoomBase):
    pass

class RoomUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=5, max_length=50)
    house_id: Optional[int] = Field(None)

class RoomResponse(RoomBase):
    id: int

    model_config = ConfigDict(from_attributes=True)