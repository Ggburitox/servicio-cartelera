from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Pelicula
from schemas import PeliculaCreate, Pelicula
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/peliculas/", response_model=Pelicula)
def crear_pelicula(pelicula: PeliculaCreate, db: Session = Depends(get_db)):
    db_pelicula = Pelicula(**pelicula.dict())
    db.add(db_pelicula)
    db.commit()
    db.refresh(db_pelicula)
    return db_pelicula

@router.get("/peliculas/", response_model=list[Pelicula])
def listar_peliculas(db: Session = Depends(get_db)):
    return db.query(Pelicula).all()

@router.get("/peliculas/{pelicula_id}", response_model=Pelicula)
def obtener_pelicula(pelicula_id: int, db: Session = Depends(get_db)):
    pelicula = db.query(Pelicula).filter(Pelicula.id == pelicula_id).first()
    if not pelicula:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    return pelicula
