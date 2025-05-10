from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routes.peliculas import router as peliculas_router

# Crea las tablas en la BD
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Cartelera", version="1.0.0")

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluye los endpoints
app.include_router(peliculas_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "ok"}
