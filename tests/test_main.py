from fastapi.testclient import TestClient

def test_create_item(client):
    response = client.post(
        "/items/",
        json={"title": "Test Item", "description": "Test Description"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Item"
    assert data["description"] == "Test Description"
    assert "id" in data

def test_read_items(client):
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_item(client):
    # First create an item
    create_response = client.post(
        "/items/",
        json={"title": "Test Item", "description": "Test Description"},
    )
    item_id = create_response.json()["id"]

    # Then read it
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Item"
    assert data["description"] == "Test Description"
