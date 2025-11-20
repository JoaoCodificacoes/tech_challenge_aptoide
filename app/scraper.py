import httpx
from typing import Optional, Dict, Any
from app.utils import format_size, format_downloads, parse_owner, format_cpu


class AptoideScraper:
    BASE_URL = "https://ws75.aptoide.com/api/7/app/get"

    async def get_app_details(self, package_name: str) -> Optional[Dict[str, Any]]:

        print(f"Connecting to {self.BASE_URL} for {package_name}...")

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(self.BASE_URL, params={"package_name": package_name})

                if response.status_code != 200:
                    print(f"Status Code: {response.status_code}")
                    return None

                raw_json = response.json()

                if (not raw_json or
                        'nodes' not in raw_json or
                        'meta' not in raw_json['nodes'] or
                        'data' not in raw_json['nodes']['meta']):
                    return None

                app_data = raw_json['nodes']['meta']['data']

                file_info = app_data.get('file', {})
                stats_info = app_data.get('stats', {})
                sig_info = file_info.get('signature', {})
                hardware_info = file_info.get('hardware', {})

                owner = parse_owner(sig_info.get('owner', ''))
                cpu_list = hardware_info.get('cpus', [])

                return {
                    "name": app_data.get('name', 'Unknown'),
                    "size": format_size(file_info.get('filesize', 0)),
                    "downloads": format_downloads(stats_info.get('downloads', 0)),
                    "version": file_info.get('vername', 'Unknown'),
                    "release_date": file_info.get('added', app_data.get('added')),
                    "min_screen": hardware_info.get('screen', 'Unknown'),
                    "supported_cpu": format_cpu(cpu_list),
                    "package_id": app_data.get('package', package_name),
                    "sha1_signature": sig_info.get('sha1', 'N/A'),
                    "developer_cn": owner.get('developer_cn', 'Unknown'),
                    "organization": owner.get('organization', 'Unknown'),
                    "local": owner.get('local', 'Unknown'),
                    "country": owner.get('country', 'Unknown'),
                    "state_city": owner.get('state_city', 'Unknown')
                }

            except Exception as e:
                print(f"Exception: {e}")
                return None