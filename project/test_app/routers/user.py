from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse

# Створюємо роутер
router = APIRouter(prefix="/users", tags=["Users"])

# Шлях для створення користувача (POST-запит)
@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # 1. Перевіряємо, чи немає вже користувача з таким email
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Користувач з таким email вже існує")
    
    # 2. Створюємо об'єкт SQLAlchemy на основі отриманих даних
    new_user = User(username=user.username, email=user.email)
    
    # 3. Зберігаємо в базу даних
    db.add(new_user)
    db.commit() # Підтверджуємо транзакцію
    db.refresh(new_user) # Оновлюємо об'єкт, щоб отримати згенерований базою `id`
    
    # 4. Повертаємо створеного користувача
    return new_user