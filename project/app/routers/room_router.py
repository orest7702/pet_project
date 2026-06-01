from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.room import RoomCreate, RoomResponse
from app.crud import room_crud, house_crud  # імпортуємо потрібні CRUD

router = APIRouter(prefix="/rooms", tags=["Rooms"])

@router.post("/", response_model=RoomResponse, status_code=status.HTTP_201_CREATED)
def create_new_room(room: RoomCreate, db: Session = Depends(get_db)):
    """
    Створення кімнати в будинку. Перевіряє, чи існує такий будинок.
    """
    # 1. ПЕРЕВІРКА: чи існує будинок, в який хочуть додати кімнату
    house = house_crud.get_house(db, house_id=room.house_id)
    if not house:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Неможливо створити кімнату. Будинку з ID {room.house_id} не існує."
        )
    
    # 2. Якщо все ок — створюємо
    return room_crud.create_room(db=db, room=room)


@router.get("/house/{house_id}", response_model=list[RoomResponse])
def get_house_rooms(house_id: int, db: Session = Depends(get_db)):
    """
    Отримання списку всіх кімнат конкретного будинку.
    """
    # Перевіряємо, чи існує сам будинок
    house = house_crud.get_house(db, house_id=house_id)
    if not house:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Будинок з ID {house_id} не знайдено."
        )
        
    return room_crud.get_rooms_by_house(db=db, house_id=house_id)


@router.delete("/{room_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_room_endpoint(room_id: int, db: Session = Depends(get_db)):
    """
    Видалення кімнати за її ID.
    """
    success = room_crud.delete_room(db=db, room_id=room_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Кімнату з ID {room_id} не знайдено."
        )
    return None