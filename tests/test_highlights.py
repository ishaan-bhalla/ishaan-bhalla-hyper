from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_highlights():
    response = client.get("/highlights")
    assert response.status_code == 200
    assert "highlights" in response.json()
