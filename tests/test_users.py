import pytest


async def test_create_user_endpoint(client):
    response = await client.post(
        "/users/",
        json={"username": "testuser", "email": "test@example.com", "password": "superpassword"}
    )

    assert response.status_code in [200, 201]

    data = response.json()
    assert data["email"] == "test@example.com"
    assert "password" not in data


async def test_login_user(client):
    # 1. Створюємо юзера
    await client.post(
        "/users/",
        json={"username": "loginuser", "email": "login@example.com", "password": "123"}
    )

    # 2. Логінимось. Оскільки ти використовуєш UserCreate, передаємо JSON з усіма полями!
    response = await client.post(
        "/auth/login",
        json={"username": "loginuser", "email": "login@example.com", "password": "123"}
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Successfully logged in"