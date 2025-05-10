from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import PeliculaDB
from app.schemas import PeliculaCreate, Pelicula
from app.database import get_db

router = APIRouter()

@router.post("/peliculas/", response_model=Pelicula, tags=["Películas"])
def crear_pelicula(pelicula: PeliculaCreate, db: Session = Depends(get_db)):
    try:
        db_pelicula = PeliculaDB(**pelicula.model_dump())
        db.add(db_pelicula)
        db.commit()
        db.refresh(db_pelicula)
        return db_pelicula
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear película: {str(e)}")

@router.get("/peliculas/", response_model=list[Pelicula], tags=["Películas"])
def listar_peliculas(db: Session = Depends(get_db)):
    return db.query(PeliculaDB).all()
