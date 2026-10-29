from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_soustraction():
    response = client.get("/soustraction", params={"a": 10, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"resultat": 6}