from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.api.endpoints import peliculas

app = FastAPI(
    title="API de Cartelera",
    version="1.0.0"
)

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crea tablas en la BD
Base.metadata.create_all(bind=engine)

# Incluye los endpoints
app.include_router(
    peliculas.router,
    prefix="/api/v1",
)
