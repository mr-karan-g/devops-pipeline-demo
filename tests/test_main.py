import pytest

from app.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"


def test_health_reports_version(client):
    res = client.get("/health")
    assert "version" in res.get_json()


def test_greet(client):
    res = client.get("/api/greet/Alice")
    assert res.status_code == 200
    assert res.get_json()["message"] == "Hello, Alice!"
