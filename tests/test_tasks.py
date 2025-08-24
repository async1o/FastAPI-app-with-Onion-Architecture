import pytest
import aiohttp
import asyncio


URLS_TO_TEST = [
    'http://localhost:8000/db GET',
    'http://localhost:8000/tasks GET',
    'http://localhost:8000/tasks POST',
    'http://localhost:8000/tasks?user_id=1 PUT',
    'http://localhost:8000/tasks?user_id=1 DELETE'
]

@pytest.fixture
async def session():
    """Создаёт общую сессию aiohttp для всех запросов."""
    async with aiohttp.ClientSession() as session:
        yield session

@pytest.mark.asyncio
@pytest.mark.parametrize("url", URLS_TO_TEST)
async def test_urls_status_200(session, url):
    url, method = url.split()
    match method:
        case 'GET':
            async with session.get(url, timeout=10) as resp:
                assert resp.status == 200, f"URL {url} вернул статус {resp.status}"
        case 'POST':
            async with session.post(url, timeout=10) as resp:
                assert resp.status == 200, f"URL {url} вернул статус {resp.status}"
        case 'PUT':
            async with session.put(url, timeout=10) as resp:
                assert resp.status == 200, f"URL {url} вернул статус {resp.status}"
        case 'DELETE':
            async with session.delete(url, timeout=10) as resp:
                assert resp.status == 200, f"URL {url} вернул статус {resp.status}"
                