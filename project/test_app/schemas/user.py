from pydantic import BaseModel

# 1. Схема для отримання даних: те, що користувач надсилає при реєстрації
class UserCreate(BaseModel):
    username: str
    email: str

# 2. Схема для відповіді: те, що наш сервер поверне після успішного створення
class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    # Це налаштування дозволяє Pydantic читати дані прямо з об'єктів SQLAlchemy
    class Config:
        from_attributes = True