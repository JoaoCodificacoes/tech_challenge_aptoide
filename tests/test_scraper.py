import pytest
import json
import os
from unittest.mock import MagicMock, patch
from app.scraper import AptoideScraper


@pytest.fixture
def scraper():
    return AptoideScraper()


@pytest.fixture
def mock_json_response():
    """Loads the LOCAL snapshot from tests/fixtures/example.json."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "fixtures", "example.json")

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


# --- TESTS ---

@pytest.mark.asyncio
async def test_get_app_details_success(scraper, mock_json_response):
    """Test successful data extraction"""
    with patch("httpx.AsyncClient.get") as mock_get:
        mock_response_obj = MagicMock()
        mock_response_obj.status_code = 200
        mock_response_obj.json.return_value = mock_json_response
        mock_get.return_value = mock_response_obj

        result = await scraper.get_app_details("com.facebook.katana")

        assert result is not None

        assert result["name"] == "Facebook"
        assert result["package_id"] == "com.facebook.katana"
        assert result["version"] == "540.0.0.44.148"
        assert result["release_date"] == "2025-11-20 12:41:04"


        assert result["size"] == "142.47 MB"
        assert result["min_screen"] == "SMALL"
        assert result["supported_cpu"] == "arm64-v8a"


        assert result["downloads"] == "2B"


        assert result["sha1_signature"] == "CC:69:EF:02:CC:1D:98:0C:EB:FC:31:4D:E9:2E:CB:63:22:AD:29:FE"


        assert result["developer_cn"] == "Meta Platforms Inc."
        assert result["organization"] == "Meta Platforms Inc."
        assert result["local"] == "Menlo Park"
        assert result["state_city"] == "California"
        assert result["country"] == "US"


@pytest.mark.asyncio
async def test_get_app_details_404(scraper):
    """Test 404 handling."""
    with patch("httpx.AsyncClient.get") as mock_get:
        mock_response_obj = MagicMock()
        mock_response_obj.status_code = 404
        mock_get.return_value = mock_response_obj

        result = await scraper.get_app_details("com.fake.app")
        assert result is None


@pytest.mark.asyncio
async def test_get_app_details_bad_json(scraper):
    """Test empty JSON handling."""
    with patch("httpx.AsyncClient.get") as mock_get:
        mock_response_obj = MagicMock()
        mock_response_obj.status_code = 200
        mock_response_obj.json.return_value = {}
        mock_get.return_value = mock_response_obj

        result = await scraper.get_app_details("com.broken.app")

        assert result is None