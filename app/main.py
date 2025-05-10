from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routes.cartelera import router as cartelera_router

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Servicio de Cartelera",
    description="API para gestionar películas",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cartelera_router, prefix="/api/v1")

@app.get("/health", tags=["Sistema"])
def health_check():
    return {"status": "ok"}
