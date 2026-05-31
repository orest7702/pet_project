from sqlalchemy.orm import Session
from app.models.house import House
from app.schemas.house import HouseCreate, HouseUpdate

def get_house(db: Session, house_id: int):
    return db.query(House).filter(House.id == house_id).first()

def get_houses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(House).offset(skip).limit(limit).all()

def get_houses_by_owner(db: Session, owner_id: int):
    return db.query(House).filter(House.owner_id == owner_id).all()

def create_house(db: Session, house: HouseCreate):
    db_house = House(**house.model_dump())
    
    db.add(db_house)
    db.commit()
    db.refresh(db_house)
    return db_house

def delete_house(db: Session, house_id: int):
    db_house = db.query(House).filter(House.id == house_id).first()
    if db_house:
        db.delete(db_house)
        db.commit()
        return True
    return False