from fastapi.testclient import TestClient
from starlette.status import *
from app import app

client = TestClient(app=app)

orders = [
    {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
    {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
    {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
    {"id": 4, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "canceled"}
]

criterion = "completed"

def test_solution_route():
    orders = [
        {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
        {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
        {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
        {"id": 4, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "canceled"}
    ]
    response = client.post(f'/solution?criterion={criterion}', json=orders)
    assert response.status_code == HTTP_200_OK
    assert response.json() == {"total_price": 1299.69}
    
def test_solution_route_error():
    orders = [
        {"id": 1, "item": "Laptop", "quantity": 0, "price": 999.99, "status": "completed"},
        {"id": 2, "item": "Smartphone", "quantity": 2, "price": 0, "status": "pending"},
        {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
        {"id": 4, "item": "Mouse", "quantity": 4, "price": -10, "status": "aaa"}
    ]
    response = client.post(f'/solution?criterion={criterion}', json=orders)
    assert response.status_code != HTTP_200_OK