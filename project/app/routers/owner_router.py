from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# Імпорти модулів проекту
from app.core.database import get_db
from app.schemas.owner import OwnerCreate, OwnerResponse
from app.crud import owner_crud as crud_owner

# Ініціалізація роутера
router = APIRouter(prefix="/owners",tags=["Owners"])

@router.get("/", response_model=List[OwnerResponse], status_code=status.HTTP_200_OK)
def read_owners(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Отримання списку всіх власників з пагінацією (skip/limit).
    """
    owners = crud_owner.get_owners(db=db, skip=skip, limit=limit)
    if not owners:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Власників не знайдено"
        )
    return owners

# 3. Ендпоінт для ОТРИМАННЯ конкретного власника за ID (GET)
@router.get("/{owner_id}", response_model=OwnerResponse, status_code=status.HTTP_200_OK)
def read_owner(owner_id: int, db: Session = Depends(get_db) ):
    """
    Отримання даних одного власника за його первинним ключем (ID).
    """
    owner = crud_owner.get_owner(db=db, owner_id=owner_id)
    if not owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Власника з ID {owner_id} не знайдено"
        )
    return owner


@router.post("/", response_model=OwnerResponse, status_code=status.HTTP_201_CREATED)
def create_owner(owner: OwnerCreate, db: Session = Depends(get_db)):
    """
    Створення нового власника. Приймає дані у форматі OwnerCreate (Pydantic-схема).
    Повертає створеного власника у форматі OwnerResponse.
    """
    return crud_owner.create_owner(db=db, owner=owner)

@router.delete("/{owner_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_owner_endpoint(owner_id: int, db: Session = Depends(get_db)):
    """
    Видалення власника за його ID.
    """
    # Викликаємо функцію з CRUD
    success = crud_owner.delete_owner(db=db, owner_id=owner_id)
    
    # Якщо такого ID немає в базі — кажемо клієнту 404 Not Found
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Власника з ID {owner_id} не знайдено"
        )
    
    # Статус 204 No Content автоматично означає успішне видалення без повернення тексту
    return None