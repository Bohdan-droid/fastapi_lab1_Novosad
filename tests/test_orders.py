import pytest

async def test_get_orders(client):
    response = await client.get("/orders/")
    assert response.status_code == 200