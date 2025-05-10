from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Pelicula
from app.schemas import PeliculaCreate, Pelicula
from app.database import get_db  # Ahora importará correctamente

router = APIRouter()

@router.post("/peliculas/", response_model=Pelicula)
def crear_pelicula(pelicula: PeliculaCreate, db: Session = Depends(get_db)):
    try:
        # Elimina el id si viene en el request (la BD lo generará)
        pelicula_data = pelicula.model_dump(exclude={'id'}) if pelicula.id else pelicula.model_dump()
        
        db_pelicula = Pelicula(**pelicula_data)
        db.add(db_pelicula)
        db.commit()
        db.refresh(db_pelicula)
        return db_pelicula
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/peliculas/", response_model=list[Pelicula])
def listar_peliculas(db: Session = Depends(get_db)):
    return db.query(Pelicula).all()
