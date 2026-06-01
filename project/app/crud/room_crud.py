from sqlalchemy.orm import Session
from app.models.room import Room
from app.schemas.room import RoomCreate

def get_room(db: Session, room_id: int):
    """Отримати одну кімнату за її ID"""
    return db.query(Room).filter(Room.id == room_id).first()

def get_rooms_by_house(db: Session, house_id: int):
    """Отримати всі кімнати, які належать конкретному будинку"""
    return db.query(Room).filter(Room.house_id == house_id).all()

def create_room(db: Session, room: RoomCreate):
    """Створити нову кімнату за допомогою model_dump"""
    db_room = Room(**room.model_dump())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

def delete_room(db: Session, room_id: int):
    """Видалити кімнату за її ID"""
    db_room = db.query(Room).filter(Room.id == room_id).first()
    if db_room:
        db.delete(db_room)
        db.commit()
        return True
    return False