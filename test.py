import json
from app import app

def test_home_status():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Tabla de Multiplicaci" in response.data

def test_home_table_generation():
    client = app.test_client()
    response = client.get("/?n=5")
    assert response.status_code == 200
    assert b"5 x 1 = 5" in response.data
    assert b"5 x 12 = 60" in response.data

def test_api_multiplicar_ok():
    client = app.test_client()
    response = client.get("/api/multiplicar?n=7")
    data = response.get_json()

    assert response.status_code == 200
    assert data["numero"] == 7
    assert data["tabla"]["1"] == 7
    assert data["tabla"]["12"] == 84

def test_api_multiplicar_missing_param():
    client = app.test_client()
    response = client.get("/api/multiplicar")
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
