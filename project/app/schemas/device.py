from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class DeviceBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    value_device: Optional[str] = Field(None, max_length=20, description="Поточне значення текстом")

class DeviceCreate(DeviceBase):
    room_id: int = Field(..., gt=0)
    # Клієнт поки не передає kind_id, бо ми його закоментували в базі
    # kind_id: int = Field(..., gt=0) 

class DeviceResponse(DeviceBase):
    id: int
    room_id: int

    model_config = ConfigDict(from_attributes=True)