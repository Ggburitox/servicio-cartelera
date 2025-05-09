from fastapi import FastAPI
from models import Base
from database import engine
from routes.cartelera import router as cartelera_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Servicio de Cartelera")

app.include_router(cartelera_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "ok"}
