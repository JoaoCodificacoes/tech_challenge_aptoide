import math


def format_size(size_bytes: int) -> str:
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s}".replace(".0", "") + f" {size_name[i]}"


def format_downloads(downloads: int) -> str:
    if downloads == 0:
        return "0"
    size_name = ("", "K", "M", "B", "T")
    # Prevent index error on more than 1000 T downloads(doubt it happens)
    i = min(int(math.floor(math.log(downloads, 1000))), len(size_name) - 1)
    p = math.pow(1000, i)
    s = round(downloads / p, 2)
    return f"{s}".replace(".0", "") + size_name[i]


def parse_owner(owner: str) -> dict:
    if not owner:
        return {}
    data = {}
    parts = [p.strip() for p in owner.split(',')]
    key_map = {
        "CN": "developer_cn",
        "O": "organization",
        "OU": "organization_unit",
        "L": "local",
        "ST": "state_city",
        "C": "country"
    }
    for part in parts:
        if '=' in part:
            key, value = part.split('=', 1)
            if key in key_map:
                data[key_map[key]] = value
    return data


def format_cpu(cpus: list[str]) -> str:
    if not cpus:
        return "Unknown"
    return ", ".join(cpus)
