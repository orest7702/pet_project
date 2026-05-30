from pydantic import BaseModel, Field
from typing import Optional

class ControlUnitBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    # Ось тут ми застосовуємо твій Regex на 12 цифр
    serial_number: str = Field(..., pattern=r"^\d{12}$")

class ControlUnitCreate(ControlUnitBase):
    house_id: int = Field(..., gt=0) # Блок керування завжди належить будинку

class ControlUnitResponse(ControlUnitBase):
    id: int
    house_id: int
    is_online: bool = False # Можна додати статус, чи підключений він зараз

    class Config:
        from_attributes = True