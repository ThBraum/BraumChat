import pytest
from httpx import AsyncClient

from braumchat_api.main import app

@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        yield ac
