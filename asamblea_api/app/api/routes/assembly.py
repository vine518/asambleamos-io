from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.agenda import Agenda
from app.models.assembly import Assembly
from app.models.representation import Representation
from app.schemas.vote import RepresentationSchema, AgendaSchema, AssemblySchema

router = APIRouter()


@router.get("/assemblies", response_model=list[AssemblySchema])
def get_assemblies(db: Session = Depends(get_db)):
    return db.query(Assembly).all()


@router.post("/assemblies", response_model=AssemblySchema)
def create_assembly(assembly: AssemblySchema, db: Session = Depends(get_db)):
    new_assembly = Assembly(**assembly.dict())
    db.add(new_assembly)
    db.commit()
    return new_assembly


@router.put("/assemblies/{id}", response_model=AssemblySchema)
def update_assembly(id: int, assembly: AssemblySchema, db: Session = Depends(get_db)):
    db_assembly = db.query(Assembly).filter(Assembly.id == id).first()
    if not db_assembly:
        raise HTTPException(status_code=404, detail="Assembly not found")
    for key, value in assembly.dict().items():
        setattr(db_assembly, key, value)
    db.commit()
    return db_assembly


@router.patch("/assemblies/{id}/status/{status}")
def change_assembly_status(id: int, status: str, db: Session = Depends(get_db)):
    db_assembly = db.query(Assembly).filter(Assembly.id == id).first()
    if not db_assembly:
        raise HTTPException(status_code=404, detail="Assembly not found")
    db_assembly.status = status
    db.commit()
    return {"message": "Status updated"}


@router.post("/assemblies/{id}/notification")
def send_assembly_notifications(id: int, notification: dict, db: Session = Depends(get_db)):
    # Logic to send notifications
    return {"message": "Notifications sent successfully"}


@router.get("/assemblies/{id}/order-of-day", response_model=list[AgendaSchema])
def get_order_of_day(id: int, db: Session = Depends(get_db)):
    agendas = db.query(Agenda).filter(Agenda.assembly_id == id).all()
    if not agendas:
        raise HTTPException(status_code=404, detail="No order of day found")
    return agendas


@router.post("/assemblies/{id}/assistance")
def register_assistance(id: int, assistance: dict, db: Session = Depends(get_db)):
    # Assistance registration logic
    return {"message": "Attendance registered"}


@router.post("/assemblies/{id}/representation", response_model=RepresentationSchema)
def register_representation(id: int, representation: RepresentationSchema, db: Session = Depends(get_db)):
    new_representation = Representation(**representation.dict())
    db.add(new_representation)
    db.commit()
    return new_representation
