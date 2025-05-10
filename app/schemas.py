from pydantic import BaseModel, Field
from datetime import datetime

class PeliculaBase(BaseModel):
    titulo: str = Field(..., example="Matrix")
    genero: str = Field(..., example="Acción")
    duracion: int = Field(..., example=120)
    fecha_estreno: datetime = Field(..., example="1999-03-31 00:00:00")

class PeliculaCreate(PeliculaBase):
    pass

class Pelicula(PeliculaBase):
    id: int

    class Config:
        from_attributes = True
