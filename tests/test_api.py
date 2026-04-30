import asyncio
import os


import pytest

from fastapi.testclient import TestClient

from main import app
from db.db import reset_tables, create_db
from services.users import UserServices
from config_db import settings
from repositories.users import UserRepositories
from schemas.users import UserAddSchema


@pytest.fixture(scope="session", autouse=True)
def setup_db():

    assert settings.MODE == "TEST"

    async def _setup():
        await create_db()
        await reset_tables()

        user = UserAddSchema(username="Bot", email="Bot@email.ru", password="12345")
        
        await UserServices(UserRepositories).add_user(user)

    asyncio.run(_setup())


@pytest.fixture(scope="session", autouse=True)
def client():
    client = TestClient(app)
    yield client


@pytest.mark.usefixtures("client")
class TestUser:
    @pytest.mark.asyncio
    async def test_get_all_users(self, client):
        response = client.get("/users")
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_add_user(self, client):
        json = {"username": "Bob", "email": "Bob@email.ru", "password": "12345"}
        response = client.post("/users", json=json)
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_update_user(self, client):
        params = {"user_id": 1}
        json = {"username": "Bob", "email": "Bob@email.ru", "password": "12345"}
        response = client.put("/users", json=json, params=params)
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_delete_user(self, client):
        response = client.delete("/users", params={"user_id": 1})
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_update_user_not_found(self, client):
        response = client.put(
            "/users",
            params={"user_id": 99999},
            json={
                "username": "Ghost",
                "email": "ghost@email.ru",
                "password": "12345",
            },
        )
        assert response.status_code == 404


@pytest.mark.usefixtures("client")
class TestTasks:
    @pytest.mark.asyncio
    async def test_get_all_users(self, client):
        response = client.get("/tasks")
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_add_user(self, client):
        user_json = {
            "username": "TaskOwner",
            "email": "taskowner@email.ru",
            "password": "12345",
        }
        user_response = client.post("/users", json=user_json)
        owner_id = user_response.json()

        json = {"text": "string", "owner_id": owner_id}
        response = client.post("/tasks", json=json)
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_update_user(self, client):
        user_json = {
            "username": "TaskOwner2",
            "email": "taskowner2@email.ru",
            "password": "12345",
        }
        owner_id = client.post("/users", json=user_json).json()
        task_id = client.post(
            "/tasks", json={"text": "before_update", "owner_id": owner_id}
        ).json()

        params = {"task_id": task_id}
        json = {"text": "string", "owner_id": owner_id}
        response = client.put("/tasks", json=json, params=params)
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_delete_user(self, client):
        owner_id = client.post(
            "/users",
            json={
                "username": "TaskOwner3",
                "email": "taskowner3@email.ru",
                "password": "12345",
            },
        ).json()
        task_id = client.post(
            "/tasks", json={"text": "for_delete", "owner_id": owner_id}
        ).json()

        response = client.delete("/tasks", params={"task_id": task_id})
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_update_task_not_found(self, client):
        owner_id = client.post(
            "/users",
            json={
                "username": "TaskOwner404",
                "email": "taskowner404@email.ru",
                "password": "12345",
            },
        ).json()
        response = client.put(
            "/tasks",
            params={"task_id": 99999},
            json={"text": "no_task", "owner_id": owner_id},
        )
        assert response.status_code == 404
