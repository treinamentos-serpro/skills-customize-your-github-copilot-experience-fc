import pytest
from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_list_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_task():
    pass


def test_create_task():
    pass


def test_missing_task():
    pass


def test_invalid_task():
    pass
