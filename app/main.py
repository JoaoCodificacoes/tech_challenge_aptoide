import asyncio

from app.scraper import AptoideScraper

if __name__ == '__main__':
    scraper = AptoideScraper()
    result = asyncio.run(scraper.get_app_details("com.facebook.katana"))
    print(result)
