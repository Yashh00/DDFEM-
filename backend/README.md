# Backend

FastAPI backend scaffold for DDFEM.

## Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

From repository root:

```bash
uvicorn backend.main:app --reload --port 8000
```

## Test

From repository root:

```bash
pytest backend/tests
```
