from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db # підстав свій шлях до get_db
from app.schemas.house import HouseCreate, HouseResponse
from app.crud import house_crud, owner_crud # імпортуємо обидва CRUD

router = APIRouter(prefix="/houses", tags=["Houses"])

@router.post("/", response_model=HouseResponse, status_code=status.HTTP_201_CREATED)
def create_new_house(house: HouseCreate, db: Session = Depends(get_db)):
    """
    Створення будинку. Автоматично перевіряє, чи існує власник.
    """
    # 1. ПЕРЕВІРКА: А чи існує взагалі такий власник в базі?
    owner = owner_crud.get_owner(db, owner_id=house.owner_id)
    if not owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Неможливо створити будинок. Власника з ID {house.owner_id} не існує."
        )
    
    # 2. Якщо власник є — створюємо будинок
    return house_crud.create_house(db=db, house=house)


@router.get("/owner/{owner_id}", response_model=list[HouseResponse])
def get_owner_houses(owner_id: int, db: Session = Depends(get_db)):
    """
    Отримання будинків ТІЛЬКИ конкретного власника (безпечний метод).
    """
    # Перевіряємо чи є такий власник
    owner = owner_crud.get_owner(db, owner_id=owner_id)
    if not owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Власника не знайдено"
        )
        
    # Повертаємо тільки його будинки
    return house_crud.get_houses_by_owner(db=db, owner_id=owner_id)

@router.delete("/{house_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_house_endpoint(house_id: int, db: Session = Depends(get_db)):
    """
    Видалення будинку за його ID.
    """
    # Викликаємо функцію з house_crud
    success = house_crud.delete_house(db=db, house_id=house_id)
    
    # Якщо такого будинку немає — віддаємо 404
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Будинок з ID {house_id} не знайдено"
        )
    
    # Статус 204 автоматично означає успіх без повернення тексту
    return None