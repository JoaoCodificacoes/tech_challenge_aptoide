from fastapi import FastAPI, Query, HTTPException
from app.scraper import AptoideScraper

app = FastAPI(
    title="Aptoide Scraper"
)
scraper = AptoideScraper()


#TODO add docs for root endpoint

@app.get("/aptoide")
async def aptoide_scraper(
        package_name: str = Query(
            ...,
            title="Package Name"
                        )):
    result = await scraper.get_app_details(package_name)
    if not result:
        raise HTTPException(status_code=404, detail="App not found")
    return result

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)