import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import models
from app.main import app
from app.core.db_conn.postgres import engine, SessionLocal, Base
from app.core.db_conn.mongo import db
from app.core.db_conn.redis import redis_client
from app.api.deps import get_db  # adjust import if needed

# Use a separate test database
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"  # For fast in-memory tests, use 'sqlite:///:memory:' if no async
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Override FastAPI's DB dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


@pytest.fixture(scope="module", autouse=True)
def create_test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

### ------------------- USER CRUD TEST ------------------- ###
def test_create_user():
    response = client.post("v1/user/create", json={
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "secure123"
    })
    assert response.status_code == 201
    assert response.json()["username"] == "testuser"


def test_read_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@example.com"

### ------------------- REMINDER CRUD TEST ------------------- ###
def test_create_reminder():
    response = client.post("/reminders/", json={
        "user_id": 1,
        "title": "Test Reminder",
        "description": "This is a test",
        "due_date": "2025-12-31T23:59:00"
    })
    assert response.status_code == 201
    assert response.json()["title"] == "Test Reminder"


def test_read_reminder():
    response = client.get("/reminders/1")
    assert response.status_code == 200
    assert response.json()["description"] == "This is a test"

### ------------------- MESSAGE CRUD TEST ------------------- ###
def test_create_message():
    response = client.post("/messages/", json={
        "user_id": 1,
        "content": "Hello World!",
        "timestamp": "2025-08-01T10:00:00"
    })
    assert response.status_code == 201
    assert response.json()["content"] == "Hello World!"


def test_read_message():
    response = client.get("/messages/1")
    assert response.status_code == 200
    assert response.json()["user_id"] == 1

### ------------------- CONTENT CRUD TEST ------------------- ###
def test_create_content():
    response = client.post("/content/", json={
        "user_id": 1,
        "title": "Test Content",
        "body": "This is test content"
    })
    assert response.status_code == 201
    assert response.json()["title"] == "Test Content"


def test_read_content():
    response = client.get("/content/1")
    assert response.status_code == 200
    assert response.json()["body"] == "This is test content"
