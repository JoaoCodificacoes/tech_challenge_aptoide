import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.mark.live
def test_live_api_end_to_end():
    """
    1. Hits  endpoint /aptoide
    2. api calls  Scraper
    3. Scraper calls Aptoide API
    4. Returns Real Data
    """

    response = client.get("/aptoide?package_name=com.facebook.katana")

    assert response.status_code == 200

    data = response.json()

    #simple assertions, because data can change
    assert data["package_id"] == "com.facebook.katana"
    assert "Facebook" in data["name"]




@pytest.mark.live
def test_live_api_404():
    """
    Verify that the real API correctly handles a missing app
    """
    response = client.get("/aptoide?package_name=com.this.does.not.exist.12345")

    assert response.status_code == 404
    assert response.json()["detail"] == "App not found"