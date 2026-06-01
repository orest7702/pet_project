from fastapi import FastAPI

from app.core.database import engine, Base

from app.routers import owner_router, house_router, room_router

# 1. Створення таблиць у базі даних (ініціалізація)
# Увага: для продакшену краще використовувати міграції (Alembic), 
# але для розробки це найшвидший спосіб створити таблиці на основі моделей.
Base.metadata.create_all(bind=engine)

# 2. Ініціалізація головного об'єкта FastAPI
app = FastAPI()


# 4. Реєстрація роутерів
# Підключаємо модулі з ендпоінтами до головного додатка
app.include_router(owner_router.router, prefix="/api/v1")
app.include_router(house_router.router, prefix="/api/v1")
app.include_router(room_router.router, prefix="/api/v1")

# 5. (Опціонально) Health Check ендпоінт для перевірки статусу сервера
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is running"}