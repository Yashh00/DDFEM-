from fastapi import FastAPI

from backend.routers.health import router as health_router

app = FastAPI(title="DDFEM Backend API")
app.include_router(health_router)


@app.get("/api")
def root() -> dict[str, str]:
    return {"message": "DDFEM backend is running"}
