from fastapi import FastAPI
from app.core.database import engine, Base
from app.models.user import User
from app.models.task import Task
from app.routers import user, task  # <--- ДОДАЛИ ІМПОРТ РОУТЕРА

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Tracker API")

# <--- ПІДКЛЮЧИЛИ РОУТЕР ДО СЕРВЕРА
app.include_router(user.router) 
app.include_router(task.router)

@app.get("/")
def read_root():
    return {"message": "Сервер працює! Таблиці успішно створені в базі даних."}