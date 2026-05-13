import pytest


async def test_get_categories(client):
    # Тестуємо отримання всіх категорій (зазвичай це публічна ручка)
    response = await client.get("/categories/")
    print("\n[GET categories]:", response.json())

    assert response.status_code == 200
    # Перевіряємо, що повернувся список
    assert isinstance(response.json(), list)


async def test_create_category(client):
    # Тестуємо створення категорії
    response = await client.post(
        "/categories/",
        json={"name": "Bassketball", "description": "Тестова категорія"}
    )
    print("\n[POST category]:", response.json())

    # Якщо тут впаде з 401 Unauthorized - значить треба буде додати токен, це нормально
    assert response.status_code in [200, 201]