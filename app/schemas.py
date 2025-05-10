from pydantic import BaseModel, Field
from datetime import datetime

class PeliculaBase(BaseModel):
    titulo: str = Field(..., example="Inception")
    genero: str = Field(..., example="Ciencia Ficción")
    duracion: int = Field(..., example=148)
    fecha_estreno: datetime = Field(..., example="2010-07-16T00:00:00")

class PeliculaCreate(PeliculaBase):
    class Config:
        schema_extra = {
            "example": {
                "titulo": "Inception",
                "genero": "Ciencia Ficción",
                "duracion": 148,
                "fecha_estreno": "2010-07-16T00:00:00"
            }
        }

class Pelicula(PeliculaBase):
    id: int

    class Config:
        from_attributes = True
        schema_extra = {
            "example": {
                "id": 1,
                "titulo": "Inception",
                "genero": "Ciencia Ficción",
                "duracion": 148,
                "fecha_estreno": "2010-07-16T00:00:00"
            }
        }
