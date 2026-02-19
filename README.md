# DDFEM Monorepo Scaffold

This repository contains a backend FastAPI service and a frontend Vite React app.

## Project Layout

- `backend/` FastAPI service plus FEM-oriented Python packages and tests.
- `frontend/` React app with API integration and build validation script.
- `Dockerfile` multi-stage production build.
- `docker-compose.yml` single-service deployment.

## Local Development

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

From repository root:

```bash
uvicorn backend.main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Testing & Validation

### Backend tests

```bash
pytest backend/tests
```

### Frontend build validation

```bash
cd frontend
npm run test:build
```

## Docker

```bash
docker compose up --build
```
