from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.models.pelicula import PeliculaDB
from app.schemas.pelicula import Pelicula, PeliculaCreate
from app.database import get_db

router = APIRouter(tags=["Películas"])

@router.post("/peliculas/", response_model=Pelicula, summary="Crear nueva película")
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

@router.get("/peliculas/", 
    response_model=List[Pelicula],
    summary="Listar todas las películas"
)
async def listar_peliculas(db: Session = Depends(get_db)):
    try:
        return db.query(PeliculaDB).all()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener películas: {str(e)}"
        )

@router.get("/peliculas/{id}", 
    response_model=Pelicula,
    summary="Obtener película por ID"
)
async def obtener_pelicula(id: int, db: Session = Depends(get_db)):
    try:
        pelicula = db.query(PeliculaDB).filter(PeliculaDB.id == id).first()
        if not pelicula:
            raise HTTPException(
                status_code=404,
                detail=f"Película con ID {id} no encontrada"
            )
        return pelicula
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener película: {str(e)}"
        )
