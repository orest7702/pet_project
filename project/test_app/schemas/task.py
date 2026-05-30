from pydantic import BaseModel
from typing import Optional

# Дані, які ми отримуємо від клієнта
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None  # Може бути порожнім (null)
    owner_id: int                      # ID користувача, якому належить завдання

# Дані, які ми повертаємо клієнту
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    is_completed: bool
    owner_id: int

    class Config:
        from_attributes = True