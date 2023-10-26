from fastapi.testclient import TestClient
from main import app
import httpx
import pytest

client = TestClient(app)

# Synchronous test
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

# Asynchronous test
@pytest.mark.asyncio
async def test_read_item():
    async with httpx.AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/items/42?query_param=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "query_param": "test"}
