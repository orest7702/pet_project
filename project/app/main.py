from fastapi import FastAPI
from app.models.base import engine, Base
from app.routers import owner_router, house_router, room_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(owner_router.router, prefix="/api/v1")
app.include_router(house_router.router, prefix="/api/v1")
app.include_router(room_router.router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is running"}