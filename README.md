# tech_challenge_aptoide

# Setup
## Prerequisites
    python 3.13

### 1. Clone repository
   ```bash
   git clone https://github.com/JoaoCodificacoes/tech_challenge_aptoide
   cd tech_challenge_aptoide
   ```

### 2. Create and activate virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```


### 3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

### 4. Run
```bash
 uvicorn app.main:app --reload
 ```

# Usage

## Endpoint
```
GET /aptoide
```

### Query Params
```
package_name
```

### Example request
```bash
curl http://localhost:8000/aptoide?package_name=com.facebook.katana
```

### Example response
 ```{
  "name": "Facebook",
  "size": "142.47 MB",
  "downloads": "2B",
  "version": "540.0.0.44.148",
  "release_date": "2025-11-20 12:41:04",
  "min_screen": "SMALL",
  "supported_cpu": "arm64-v8a",
  "package_id": "com.facebook.katana",
  "sha1_signature": "CC:69:EF:02:CC:1D:98:0C:EB:FC:31:4D:E9:2E:CB:63:22:AD:29:FE",
  "developer_cn": "Meta Platforms Inc.",
  "organization": "Meta Platforms Inc.",
  "local": "Menlo Park",
  "country": "US",
  "state_city": "California"
}
```

# Testing 

## Run Unit and E2E tests
 Runs logic tests using local fixtures and mock
```bash
 python -m pytest -m "not live"
```

## Run Integration tests
 Hits the live Aptoide API
```bash
 python -m pytest -m live
```

# Design Decision and Assumptions

## 1. API Scraping vs HTML Scraping
I chose to look for the API endpoint first because if avalaible it's the more reliable and faster way than scraping the HTML.

## 2. Service oriented architecture
I chose to use a service oriented architecture because it's the most scalable way to handle this kind of scenario.
## 3. Scalabilty
    
## 4. Testing
I chose to do live tests too because when scraping it helps to check if there was any change in the data structure or api url





