from fastapi import FastAPI
from app.api.endpoints import peliculas
from app.database import engine, Base

app = FastAPI()

# Crea las tablas
Base.metadata.create_all(bind=engine)

# Incluye los routers
app.include_router(peliculas.router, prefix="/api/v1")
