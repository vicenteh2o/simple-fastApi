from fastapi.testclient import TestClient
from main import app, items

client = TestClient(app)

def setup_function():
    # Clear the items list before each test
    items.clear()

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []

def test_create_item():
    response = client.post(
        "/items",
        json={"text": "Test item", "is_done": False}
    )
    assert response.status_code == 200
    assert response.json() == [{"text": "Test item", "is_done": False}]

def test_get_item_by_id():
    # First create an item
    client.post("/items", json={"text": "Test item", "is_done": False})

    # Then get it by ID
    response = client.get("/items/0")
    assert response.status_code == 200
    assert response.json() == {"text": "Test item", "is_done": False}

def test_get_nonexistent_item():
    # test getting an item that does not exist
    response = client.get("/items/999")
    assert response.status_code == 404