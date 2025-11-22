import logging
import httpx
from contextlib import asynccontextmanager
from fastapi import FastAPI, Query, HTTPException
from app.scraper import AptoideScraper

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api")


http_client: httpx.AsyncClient = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifecycle Manager:
    1. Startup: Create ONE persistent HTTP client.
    2. Shutdown: Close it cleanly.
    """
    global http_client
    logger.info("Initializing connection")

    # Reusing this client prevents creating a new SSL handshake for every request
    http_client = httpx.AsyncClient(timeout=10.0)
    yield

    logger.info("Closing connection")
    await http_client.aclose()


app = FastAPI(
    title="Aptoide Scraper API",
    lifespan=lifespan
)

@app.get("/aptoide")
async def aptoide_scraper(
        package_name: str = Query(
            ...,
            title="Package Name",
        )
):
    scraper = AptoideScraper(http_client)

    result = await scraper.get_app_details(package_name)

    if not result:
        raise HTTPException(status_code=404, detail="App not found")

    return result


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)