import pytest
import httpx
from app.scraper import AptoideScraper

@pytest.mark.asyncio
@pytest.mark.live
async def test_live_connection():
    """
    Hits the real Aptoide API to ensure the URL works.
    """

    async with httpx.AsyncClient() as client:

        scraper = AptoideScraper(client)

        result = await scraper.get_app_details("com.facebook.katana")

        # Simple asserts, because data can change
        assert result is not None
        assert result["package_id"] == "com.facebook.katana"
        assert "Facebook" in result["name"]