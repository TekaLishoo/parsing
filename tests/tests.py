import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient


@pytest.fixture
def api_client():
    app = FastAPI()
    client = TestClient(app)
    return client


def test_get_lamoda_products(api_client):
    response = api_client.get("/lamoda/")
    assert response.status_code == 404


def test_get_twitch_products(api_client):
    response = api_client.get("/twitch/")
    assert response.status_code == 404
