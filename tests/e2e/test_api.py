from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
from app.main import app

client = TestClient(app)
app.state.http_client = AsyncMock()

MOCK_RESULT = {
    "name": "Facebook",
    "size": "142.47 MB",
    "downloads": "2B",
    "package_id": "com.facebook.katana",
    "version": "1.0",
    "supported_cpu": "arm64"
}


@patch("app.scraper.AptoideScraper.get_app_details", new_callable=AsyncMock)
def test_get_package_info_success(mock_get_details):
    """
    Test that the API returns 200 and the correct JSON
    """
    mock_get_details.return_value = MOCK_RESULT

    response = client.get("/aptoide?package_name=com.facebook.katana")

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Facebook"
    assert data["downloads"] == "2B"


@patch("app.scraper.AptoideScraper.get_app_details", new_callable=AsyncMock)
def test_get_package_info_404(mock_get_details):
    """
    Test that the API returns 404 and specific error message when app is missing.
    """
    mock_get_details.return_value = None

    response = client.get("/aptoide?package_name=com.ghost.app")

    assert response.status_code == 404
    assert response.json()["detail"] == "App not found"


def test_validation_error():
    """
    Test that missing the query parameter triggers a 422 error.
    """
    response = client.get("/aptoide")

    assert response.status_code == 422
    assert "Field required" in response.text