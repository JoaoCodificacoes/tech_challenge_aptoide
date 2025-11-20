import httpx
import asyncio
import json


class AptoideScraper:
    BASE_URL = "https://ws75.aptoide.com/api/7/app/get"

    async def get_raw_json(self, package_name: str):

        print(f"Connecting to {self.BASE_URL} for {package_name}...")

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(self.BASE_URL, params={"package_name": package_name})


                print(f"Status Code: {response.status_code}")

                if response.status_code == 200:
                    raw_json = response.json()

                    data = raw_json['nodes']['meta']['data']


                    filename = "raw_response.json"
                    with open(filename, "w", encoding="utf-8") as f:
                        json.dump(raw_json, f, indent=2)


                else:
                    print("Error: Failed to fetch data.")

            except Exception as e:
                print(f"Exception: {e}")


if __name__ == "__main__":
    scraper = AptoideScraper()
    asyncio.run(scraper.get_raw_json("com.facebook.katana"))
