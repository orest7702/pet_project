from sqlalchemy.orm import Session

from app.models.owner import Owner
# Імпорт Pydantic-схеми (валідовані дані)
from app.schemas.owner import OwnerCreate

def get_owner(db: Session, owner_id: int):
    return db.query(Owner).filter(Owner.id == owner_id).first()

def get_owners(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Owner).offset(skip).limit(limit).all()

def create_owner(db: Session, owner: OwnerCreate):
    db_owner = Owner(**owner.model_dump())
    
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner

def delete_owner(db: Session, owner_id: int):
    # Шукаємо власника в базі
    db_owner = db.query(Owner).filter(Owner.id == owner_id).first()
    if db_owner:
        db.delete(db_owner)  # Маркуємо об'єкт на видалення
        db.commit()          # Зберігаємо зміни в базі
        return True
    return False