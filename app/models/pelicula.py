from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime

class PeliculaDB(Base):
    __tablename__ = "peliculas"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    genero = Column(String(50))
    duracion = Column(Integer)
    fecha_estreno = Column(DateTime)
