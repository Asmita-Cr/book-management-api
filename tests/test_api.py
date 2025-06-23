
import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_recommendation_endpoint(client):
    response = client.get('/recommend?query=Harry')
    assert response.status_code == 200
    assert b"Harry" in response.data
