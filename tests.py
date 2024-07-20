import pytest
from fastapi.testclient import TestClient

from main import app
from cities import get_city, suggest_city

@pytest.mark.asyncio
async def test_suggest_city():
    cities = await suggest_city('москва хабар')
    expected_cities = ['г Москва, ул Хабаровская', 'г Москва, поселение Московский, г Московский, ул Хабарова', 'г Москва, ул Хабаровская, д 1', 'г Москва, ул Хабаровская, д 2', 'г Москва, ул Хабаровская, д 2А', 'г Москва, ул Хабаровская, д 3', 'г Москва, ул Хабаровская, д 4', 'г Москва, ул Хабаровская, д 4А', 'г Москва, ул Хабаровская, д 5', 'г Москва, ул Хабаровская, д 8']
    assert cities == expected_cities

client = TestClient(app)

