from app.utils import format_size, format_downloads, parse_owner, format_cpu


class TestSizeFormatter:

    def test_zero(self):
        assert format_size(0) == "0B"

    def test_mb_conversion(self):
        assert format_size(159907840) == "152.5 MB"

    def test_gb_conversion(self):
        assert format_size(1073741824) == "1 GB"

    def test_cleanup_decimal(self):
        #100.0 MB to 100 MB
        assert format_size(104857600) == "100 MB"


class TestDownloadFormatter:

    def test_zero(self):
        assert format_downloads(0) == "0"

    def test_thousands(self):
        assert format_downloads(5000) == "5K"

    def test_billions(self):
        assert format_downloads(2000000000) == "2B"

    def test_trillions_safety(self):
        assert format_downloads(10 ** 15) == "1000T"


class TestCPUFormatter:

    def test_multiple_arch(self):
        assert format_cpu(["arm64", "x86"]) == "arm64, x86"

    def test_single_arch(self):
        assert format_cpu(["arm64"]) == "arm64"

    def test_empty_list(self):
        assert format_cpu([]) == "Unknown"


class TestOwnerParser:

    def test_full_string(self):
        raw = "CN=Facebook, C=US, O=Meta"
        data = parse_owner(raw)
        assert data["developer_cn"] == "Facebook"
        assert data["country"] == "US"
        assert data["organization"] == "Meta"

    def test_partial_string(self):
        raw = "CN=IndieDev"
        data = parse_owner(raw)
        assert data["developer_cn"] == "IndieDev"
        assert "country" not in data

    def test_empty_string(self):
        assert parse_owner("") == {}