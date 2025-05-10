from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.pelicula import PeliculaDB
from app.schemas.pelicula import PeliculaCreate, Pelicula
from app.database import get_db

router = APIRouter()

@router.post("/peliculas/", response_model=Pelicula)
async def crear_pelicula(
    pelicula: PeliculaCreate, 
    db: Session = Depends(get_db)
):
    try:
        db_pelicula = PeliculaDB(**pelicula.model_dump())
        db.add(db_pelicula)
        db.commit()
        db.refresh(db_pelicula)
        return db_pelicula
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Error al crear película: {str(e)}"
        )
