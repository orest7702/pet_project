from sqlalchemy.orm import Session

from app.models.owner import Owner
# Імпорт Pydantic-схеми (валідовані дані)
from app.schemas.owner import OwnerCreate

def get_owner(db: Session, owner_id: int):
    return db.query(Owner).filter(Owner.id == owner_id).first()

def get_owners(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Owner).offset(skip).limit(limit).all()

def create_owner(db: Session, owner: OwnerCreate):
    # 1. Перетворення Pydantic-схеми на об'єкт бази даних (SQLAlchemy модель)
    db_owner = Owner(**owner.model_dump())
    
    db.add(db_owner)
    
    # 3. Фіксація транзакції (фізичний запис у базу)
    db.commit()
    
    # 4. Оновлення об'єкта даними з бази
    db.refresh(db_owner)
    
    # 5. Повернення готового об'єкта (який вже має ID)
    return db_owner