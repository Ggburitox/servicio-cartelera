from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Pelicula(Base):
    __tablename__ = "peliculas"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    genero = Column(String(50))
    duracion = Column(Integer)  # Minutos
    fecha_estreno = Column(DateTime)