from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class PeliculaDB(Base):
    __tablename__ = "peliculas"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    genero = Column(String(50))
    duracion = Column(Integer)
    fecha_estreno = Column(DateTime)
