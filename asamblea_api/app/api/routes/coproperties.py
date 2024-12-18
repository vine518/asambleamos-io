from http.client import HTTPException

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.condominium import Condominium
from app.schemas.vote import CondominiumSchema

router = APIRouter()

@router.get("/coproproperties", response_model=list[CondominiumSchema])
def get_coproperties(db: Session = Depends(get_db)):
    return db.query(Condominium).all()


@router.post("/coproproperties", response_model=CondominiumSchema)
def create_coproperty(coproperty: CondominiumSchema, db: Session = Depends(get_db)):
    new_coproperty = Condominium(**coproperty.dict())
    db.add(new_coproperty)
    db.commit()
    return new_coproperty


@router.put("/coproproperties/{id}", response_model=CondominiumSchema)
def update_coproperty(id: int, copropiedad: CondominiumSchema, db: Session = Depends(get_db)):
    db_coproperty = db.query(Condominium).filter(Condominium.id == id).first()
    if not db_coproperty:
        raise HTTPException(status_code=404, detail="Coproperty not found")
    for key, value in copropiedad.dict().items():
        setattr(db_coproperty, key, value)
    db.commit()
    return db_coproperty


def calculate_coefficient(coproperty):
    pass


@router.get("/coproproperties/{id}/coeficient")
def get_coproperty_coefficient(id: int, db: Session = Depends(get_db)):
    coproperty = db.query(Condominium).filter(Condominium.id == id).first()
    if not coproperty:
        raise HTTPException(status_code=404, detail="Coproperty not found")
    return {"coefficient": calculate_coefficient(coproperty)}
