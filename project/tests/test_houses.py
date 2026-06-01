import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Тимчасові змінні для збереження ID між тестами
owner_id = None
house_id = None

def test_setup_owner_for_house():
    """Створюємо власника, якому будемо додавати будинок"""
    global owner_id
    owner_data = {
        "name": "Остап",
        "first_name": "Будинковий",
        "person_nomber": 555444333
    }
    response = client.post("/api/v1/owners/", json=owner_data)
    assert response.status_code == 201
    owner_id = response.json()["id"]


def test_create_house():
    """Тест успішного створення будинку для створеного власника"""
    global house_id
    house_data = {
        "name": "Заміська Дача",
        "address": "вул. Зелена, 15, Львів",
        "owner_id": owner_id
    }
    response = client.post("/api/v1/houses/", json=house_data)
    assert response.status_code == 201
    
    data = response.json()
    assert "id" in data
    assert data["name"] == house_data["name"]
    assert data["owner_id"] == owner_id
    house_id = data["id"]


def test_create_house_with_fake_owner():
    """Тест перевірки безпеки: не можна створити будинок для неіснуючого власника"""
    fake_house_data = {
        "name": "Примарний замок",
        "address": "Вул. Невідома, 1",
        "owner_id": 999999  # такого ID точно немає
    }
    response = client.post("/api/v1/houses/", json=fake_house_data)
    # Наш роутер має повернути 404
    assert response.status_code == 404


def test_get_owner_houses():
    """Тест отримання списку будинків конкретного власника"""
    response = client.get(f"/api/v1/houses/owner/{owner_id}")
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["id"] == house_id


def test_cascade_deletion():
    """Тест магії CASCADE: видаляємо власника — будинок має зникнути автоматично"""
    # 1. Видаляємо власника
    delete_owner_res = client.delete(f"/api/v1/owners/{owner_id}")
    assert delete_owner_res.status_code == 204
    
    # 2. Перевіряємо його список будинків. Роутер поверне 404, бо власника вже немає
    get_houses_res = client.get(f"/api/v1/houses/owner/{owner_id}")
    assert get_houses_res.status_code == 404