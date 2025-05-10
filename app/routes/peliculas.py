from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Pelicula
from app.schemas import PeliculaCreate, Pelicula
from app.database import get_db  # Ahora importará correctamente

router = APIRouter()

@router.post("/peliculas/", response_model=Pelicula)
def crear_pelicula(pelicula: PeliculaCreate, db: Session = Depends(get_db)):
    try:
        db_pelicula = PeliculaDB(
            titulo=pelicula.titulo,
            genero=pelicula.genero,
            duracion=pelicula.duracion,
            fecha_estreno=pelicula.fecha_estreno
        )
        
        db.add(db_pelicula)
        db.commit()
        db.refresh(db_pelicula)
    
        return Pelicula(
            id=db_pelicula.id,
            titulo=db_pelicula.titulo,
            genero=db_pelicula.genero,
            duracion=db_pelicula.duracion,
            fecha_estreno=db_pelicula.fecha_estreno
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/peliculas/", response_model=list[Pelicula])
def listar_peliculas(db: Session = Depends(get_db)):
    return db.query(Pelicula).all()
