import pytest

async def test_get_profiles(client):
    response = await client.get("/profiles/")
    assert response.status_code == 200