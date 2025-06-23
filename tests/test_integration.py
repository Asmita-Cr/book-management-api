
import pytest
from app import app

def test_database_connection():
    tester = app.test_client()
    response = tester.get('/books')
    assert response.status_code == 200
    assert b"title" in response.data  # crude check for book data presence
