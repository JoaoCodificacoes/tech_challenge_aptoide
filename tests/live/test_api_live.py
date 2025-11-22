import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():

    # trigger lifespan
    with TestClient(app) as c:
        yield c



@pytest.mark.live
def test_live_api_end_to_end(client):
    """
    1. Hits endpoint /aptoide
    2. API calls Scraper
    3. Scraper calls Aptoide API
    4. Returns real Data
    """
    response = client.get("/aptoide?package_name=com.facebook.katana")

    assert response.status_code == 200

    data = response.json()
    # Simple assertions because data changes
    assert data["package_id"] == "com.facebook.katana"
    assert "Facebook" in data["name"]

    assert "MB" in data["size"] or "GB" in data["size"]
    assert data["downloads"].endswith("B") or data["downloads"].endswith("M")


@pytest.mark.live
def test_live_api_404(client):
    """
    Verify that the real API correctly handles a missing app
    """

    response = client.get("/aptoide?package_name=com.this.does.not.exist.12345")

    assert response.status_code == 404
    assert response.json()["detail"] == "App not found"