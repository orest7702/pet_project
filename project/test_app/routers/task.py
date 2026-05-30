from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.task import Task
from app.models.user import User
from app.schemas.task import TaskCreate, TaskResponse

# Створюємо роутер для завдань
router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    # 1. Шукаємо користувача з таким ID в базі
    user = db.query(User).filter(User.id == task.owner_id).first()
    
    # Якщо користувача немає — викидаємо помилку 404
    if not user:
        raise HTTPException(status_code=404, detail="Користувач не знайдений")
    
    # 2. Створюємо об'єкт завдання
    new_task = Task(
        title=task.title,
        description=task.description,
        owner_id=task.owner_id
    )
    
    # 3. Зберігаємо в БД
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return new_task