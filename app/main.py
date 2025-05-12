from fastapi import FastAPI
from app.api.geocode import router as geocode_router

app = FastAPI(title="Alora Geo")

@app.get("/health")
async def health():
    return {"status": "ok"}

app.include_router(geocode_router, prefix="/api")