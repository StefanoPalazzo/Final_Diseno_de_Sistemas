import pytest
from flask import Flask, jsonify, request
from Services.detect_mutant import is_mutant
from Controllers.mutant_controller import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_root(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert rv.data == b'root'

def test_get_mutantes(client):
    rv = client.get('/mutantes')
    assert rv.status_code == 200

def test_check_dna_invalid_request(client):
    """Test when the request is malformed (missing 'dna')"""
    rv = client.post('/mutant', json={})
    assert rv.status_code == 400
    assert rv.json == {"error": "Solicitud mal formada: se esperaba un objeto JSON con la clave 'dna'."}


def test_check_dna_mutant(client):
    dna = ["ATCGTG",
        "CACTTC",
        "TTATGT",
        "AGATCG",
        "TCAGGA",
        "ATAACT"]
    rv = client.post('/mutant', json={"dna": dna})
    assert rv.status_code == 409
