import pytest
from app.scraper import AptoideScraper


@pytest.mark.asyncio
@pytest.mark.live
async def test_live_connection():
    """
    Hits Aptoide API to ensure the URL works.
    """
    scraper = AptoideScraper()

    result = await scraper.get_app_details("com.facebook.katana")

    # Simple checks to check connection, because data changes
    assert result is not None
    assert result["package_id"] == "com.facebook.katana"
    assert "Facebook" in result["name"]