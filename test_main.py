from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_soustraction():
    """Soustraction nominale."""
    response = client.get("/soustraction", params={"a": 10, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"resultat": 6}


def test_soustraction_negative():
    """Résultat négatif."""
    response = client.get("/soustraction", params={"a": 4, "b": 6})
    assert response.json() == {"resultat": -2}


def test_soustraction_zero():
    """Soustraction avec zéro."""
    response = client.get("/soustraction", params={"a": 5, "b": 0})
    assert response.json() == {"resultat": 5}


def test_soustraction_param_invalide():
    """Paramètre non numérique : erreur de validation."""
    response = client.get("/soustraction", params={"a": "abc", "b": 4})
    assert response.status_code == 422


def test_soustraction_param_manquant():
    """Paramètre manquant : erreur de validation."""
    response = client.get("/soustraction", params={"a": 4})
    assert response.status_code == 422


def test_addition():
    """Addition : on vérifie le statut."""
    response = client.get("/addition", params={"a": 4, "b": 6})
    assert response.status_code == 200

def test_division_par_zero():
    """Déclenche la branche except."""
    response = client.get("/division", params={"a": 4, "b": 0})
    assert response.status_code in (400, 500)