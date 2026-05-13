import pytest


async def test_create_and_get_products(client):
    # 0. ПРОХОДИМО АВТОРИЗАЦІЮ
    # Спочатку реєструємо тестового адміна
    await client.post(
        "/users/",
        json={"username": "admin", "email": "admin@example.com", "password": "123"}
    )
    # Потім логінимось. Клієнт отримає токен і автоматично збереже його в кукі!
    await client.post(
        "/auth/login",
        json={"username": "admin", "email": "admin@example.com", "password": "123"}
    )

    # 1. Тепер ми "залогінені". Створюємо категорію спокійно
    cat_response = await client.post(
        "/categories/",
        json={"name": "Взуття", "description": "Спортивне взуття"}
    )
    category_id = cat_response.json()["id"]

    # 2. Створюємо продукт (змінили name на title)
    prod_response = await client.post(
        "/products/",
        json={
            "title": "Кросівки Nike Kobe 8",
            "description": "Професійні баскетбольні кросівки",
            "price": 9500.50,
            "category_id": category_id
        }
    )
    print("\n[POST ПРОДУКТ]:", prod_response.json())
    assert prod_response.status_code in [200, 201]

    # 3. Перевіряємо, чи віддає сервер список продуктів
    get_response = await client.get("/products/")
    print("\n[GET ПРОДУКТИ]:", get_response.json())

    assert get_response.status_code == 200
    assert len(get_response.json()) > 0