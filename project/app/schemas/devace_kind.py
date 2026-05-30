from pydantic import BaseModel, Field
from typing import Optional

class DeviceKindBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Назва типу (напр. Термометр)")
    unit: Optional[str] = Field(None, max_length=20, description="Одиниці виміру (напр. °C, %)")
    marking: Optional[str] = Field(None, description="Додатковий опис або маркування")

class DeviceKindCreate(DeviceKindBase):
    pass  # При створенні нам достатньо полів з Base

class DeviceKindResponse(DeviceKindBase):
    id: int

    class Config:
        from_attributes = True # Дозволяє працювати з моделями SQLAlchemy