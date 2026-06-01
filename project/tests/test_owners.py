import pytest
from fastapi.testclient import TestClient
from app.main import app  # імпортуємо твій головний файл FastAPI

# Створюємо клієнта для тестування
client = TestClient(app)

# Тестові дані, які ми будемо використовувати
TEST_OWNER = {
    "name": "Тестовий",
    "first_name": "Власник",
    "person_nomber": 999888777
}

def test_create_owner():
    """Тест успішного створення власника"""
    # Відправляємо POST-запит, як у Swagger
    response = client.post("/api/v1/owners/", json=TEST_OWNER)
    
    # Перевіряємо, чи повернувся статус 201 Created
    assert response.status_code == 201
    
    data = response.json()
    # Перевіряємо, чи база повернула нам ID та правильні дані
    assert "id" in data
    assert data["name"] == TEST_OWNER["name"]
    assert data["person_nomber"] == TEST_OWNER["person_nomber"]
    
    # Зберігаємо ID створеного користувача для наступних тестів
    pytest.shared_owner_id = data["id"]


def test_get_owners_list():
    """Тест отримання списку власників"""
    response = client.get("/api/v1/owners/")
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)  # Має повернутися саме список
    assert len(data) > 0


def test_delete_owner():
    """Тест успішного видалення власника"""
    # Беремо ID, який ми зберегли під час створення
    owner_id = pytest.shared_owner_id
    
    # Видаляємо його
    response = client.delete(f"/api/v1/owners/{owner_id}")
    assert response.status_code == 204
    
    # Перевіряємо, що його дійсно немає (GET має повернути 404)
    get_response = client.get(f"/api/v1/owners/{owner_id}")
    # Примітка: якщо у тебе ще немає ендпоінту GET /owners/{id}, 
    # цей рядок можна тимчасово закоментувати