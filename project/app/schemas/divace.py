from pydantic import BaseModel, Field
from typing import Optional

class DeviceBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    value_divace: Optional[str] = Field(None, max_length=20, description="Поточне значення текстом")

class DeviceCreate(DeviceBase):
    # При створенні пристрою нам треба знати, до якого ТИПУ він належить
    kind_id: int = Field(..., gt=0)
    # room_id ми можемо передавати тут, або брати з URL (як ми обговорювали)
    room_id: int = Field(..., gt=0)

class DeviceResponse(DeviceBase):
    id: int
    kind_id: int
    room_id: int

    class Config:
        from_attributes = True