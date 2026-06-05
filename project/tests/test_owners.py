def test_create_owner_success(client):
    """
    Тест успішного створення нового власника з реальними полями схеми.
    """
    owner_data = {
        "name": "Шевченко",
        "first_name": "Тарас",
        "person_nomber": 12345
    }
    
    response = client.post("/api/v1/owners/", json=owner_data)
    
    assert response.status_code == 201
    
    json_data = response.json()
    assert json_data["name"] == "Шевченко"
    assert json_data["first_name"] == "Тарас"
    assert json_data["person_nomber"] == 12345
    assert "id" in json_data


def test_read_owner_by_id_success(client, sample_owner):
    """
    Тест отримання конкретного власника за його ID.
    """
    response = client.get(f"/api/v1/owners/{sample_owner.id}")
    
    assert response.status_code == 200
    
    json_data = response.json()
    assert json_data["id"] == sample_owner.id
    assert json_data["name"] == sample_owner.name
    assert json_data["person_nomber"] == sample_owner.person_nomber


def test_read_all_owners_success(client, sample_owner):
    """
    Тест отримання списку всіх власників.
    """
    response = client.get("/api/v1/owners/")
    
    assert response.status_code == 200
    
    json_data = response.json()
    assert len(json_data) == 1
    assert json_data[0]["id"] == sample_owner.id


def test_delete_owner_success(client, sample_owner):
    """
    Тест успішного видалення власника.
    """
    response = client.delete(f"/api/v1/owners/{sample_owner.id}")
    
    assert response.status_code == 204