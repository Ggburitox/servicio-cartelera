from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Pelicula
from app.schemas import PeliculaCreate, Pelicula
from app.database import get_db  # Ahora importará correctamente

router = APIRouter()

@router.post("/peliculas/", response_model=Pelicula)
def crear_pelicula(pelicula: PeliculaCreate, db: Session = Depends(get_db)):
    try:
        db_pelicula = Pelicula(**pelicula.model_dump())  # Cambia esto
        db.add(db_pelicula)
        db.commit()
        db.refresh(db_pelicula)
        return db_pelicula  # Ahora incluirá el id generado
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/peliculas/", response_model=list[Pelicula])
def listar_peliculas(db: Session = Depends(get_db)):
    return db.query(Pelicula).all()
