from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class PeliculaBase(BaseModel):
    titulo: str = Field(..., example="Matrix")
    genero: str = Field(..., example="Acción")
    duracion: int = Field(..., example=120)
    fecha_estreno: datetime = Field(..., example="1999-03-31T00:00:00")

class PeliculaCreate(PeliculaBase):
    pass

class Pelicula(PeliculaBase):
    id: int
    
    class Config:
        from_attributes = True

# Opcional para respuestas de lista
class PeliculaList(BaseModel):
    peliculas: List[Pelicula]
