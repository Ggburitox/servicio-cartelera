from pydantic import BaseModel
from datetime import datetime

class PeliculaBase(BaseModel):
    titulo: str
    genero: str
    duracion: int
    fecha_estreno: datetime

class PeliculaCreate(PeliculaBase):
    pass

class Pelicula(PeliculaBase):
    id: int

    class Config:
        from_attributes = True
