from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.unit import Unit
from app.schemas.vote import UnitSchema

router = APIRouter()


@router.get("/unidades-inmobiliarias", response_model=list[UnitSchema])
def get_units(db: Session = Depends(get_db)):
    return db.query(Unit).all()


@router.post("/unidades-inmobiliarias", response_model=UnitSchema)
def create_unit(unit: UnitSchema, db: Session = Depends(get_db)):
    new_unit = Unit(**unit.dict())
    db.add(new_unit)
    db.commit()
    return new_unit
