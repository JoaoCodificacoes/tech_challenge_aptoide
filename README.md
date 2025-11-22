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

# Design Decision

## 1. API Scraping vs HTML Scraping
- **Reliability:** APIs change less frequently than HTML DOM structures.
- **Performance:** Returning JSON is significantly faster and consumes less bandwidth than parsing full HTML pages.
- **Stability:** Avoids issues with dynamic JavaScript rendering.

## 3. Scalability and Architecture
- **Single Client Instance:** Instead of opening a new connection for every single request (which is slow), I use FastAPI's `lifespan` to create one shared `httpx` client when the app starts. This keeps the connection open and makes scraping much faster.
- **Dependency Injection:** I inject this client into the scraper, which makes the code cleaner and easier to test.  
    
## 4. Testing
- **Unit Tests (`tests/unit`):** Fast, offline tests using mocked responses. This validates that *my parsing logic* is correct, assuming the data format hasn't changed.
- **Live Tests (`tests/live`):** Slower, integration tests that hit the *real* Aptoide API. These are crucial for a scraper to detect if the external API schema has changed.





