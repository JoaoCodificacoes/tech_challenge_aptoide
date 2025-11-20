import httpx
import asyncio


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

                    app_data = raw_json['nodes']['meta']['data']

                    file_info = app_data.get('file', {})
                    stats_info = app_data.get('stats', {})
                    sig_info = file_info.get('signature', {})
                    hardware_info = file_info.get('hardware', {})

                    name = app_data.get('name', 'None')
                    package_id = app_data.get('package', 'None')
                    version = file_info.get('vername', 'None')
                    release_date = file_info.get('added', 'None')
                    min_screen = hardware_info.get('screen', 'None')
                    sha1 = sig_info.get('sha1', 'None')


                    # These need additional formatting
                    size_raw = file_info.get('filesize', -1)
                    downloads_raw = stats_info.get('downloads', -1)
                    owner_string = sig_info.get('owner', 'None')
                    cpu_list = hardware_info.get('cpus', [])

                    print(f"name: {name}")
                    print(f"Raw Size: {size_raw}")
                    print(f"Raw Downloads: {downloads_raw}")
                    print(f"version: {version}")
                    print(f"release date: {release_date}")
                    print(f"min_screen: {min_screen}")
                    print(f"raw supported cpus: {cpu_list}")
                    print(f"package_id: {package_id}")
                    print(f"sha1_signature: {sha1}")
                    print(f"Raw Owner: {owner_string}")


                else:
                    print("Error: Failed to fetch data.")

            except Exception as e:
                print(f"Exception: {e}")


if __name__ == "__main__":
    scraper = AptoideScraper()
    asyncio.run(scraper.get_raw_json("com.facebook.katana"))
