# tech_challenge_aptoide

# Setup
## Prerequisites
python 3.9

### 1. Clone repository
``git clone https://github.com/JoaoCodificacoes/tech_challenge_aptoide``

### 2. Create and activate virtual environment
``python -m venv venv``
``source venv/bin/activate``

### 3. Install dependencies
``pip install -r requirements.txt``

### 4. Run
``uvicorn app.main:app --reload``

# Usage

## Endpoint
``GET /aptoide``

### Query Params
``package_name``

### Example request
``curl http://localhost:8000/aptoide?package_name=com.facebook.katana``

### Example response
 







