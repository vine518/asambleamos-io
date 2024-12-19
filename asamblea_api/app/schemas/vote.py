from enum import Enum

from pydantic import BaseModel, Field

from app.models.voting import VotingState


class VoteInput(BaseModel):
    voter_id: int = Field(..., gt=0)
    question_id: int = Field(..., gt=0)
    vote_option: str = Field(..., min_length=1, max_length=50)
    remarks: str = Field(None, max_length=255)


from pydantic import BaseModel, EmailStr
from typing import Optional, List

# User Schemas
class UserBase(BaseModel):
    fullName: str
    telephone: str
    email: EmailStr
    type: str
    needs_assistance: Optional[bool] = False

class UserSchema(UserBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True

# Assembly Schemas
class AssemblyBase(BaseModel):
    nombre: str
    fecha: str
    copropiedad_id: int
    estado: str
    description: Optional[str]

class AssemblySchema(AssemblyBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True

# Copropiedad Schemas
class CopropiedadBase(BaseModel):
    nombre: str
    direccion: str
    representante_legal_id: int
    area_construida: float

class CopropiedadSchema(CopropiedadBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True

# Unit Schemas
class UnitBase(BaseModel):
    tipo: str
    numero: str
    area_construida: float
    coeficiente: int
    propietario_id: int
    copropiedad_id: int

class UnitSchema(UnitBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True

# Votation Schemas
class VotationBase(BaseModel):
    description: str
    assembly_id: int
    state: VotingState
    result: Optional[str]

class VotationSchema(VotationBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True

# Vote Schemas
class VoteBase(BaseModel):
    usuario_id: int
    pregunta_id: int
    respuesta: str

class VoteSchema(VoteBase):
    id: int
    timestamp: str

    class Config:
        orm_mode = True
        from_attributes = True

# Notification Schema
class NotificationSchema(BaseModel):
    tipo: str
    mensaje: str
    destinatarios: List[str]

# Representation Schema
class RepresentationSchema(BaseModel):
    apoderado_id: int
    propietario_id: int
    asamblea_id: int


# Agenda Schemas
class AgendaBase(BaseModel):
    descripcion: str
    asamblea_id: int
    orden: int

class AgendaSchema(AgendaBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True

# Voting Question Schemas
class VotingQuestionBase(BaseModel):
    descripcion: str
    orden_dia_id: int

class VotingQuestionSchema(VotingQuestionBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True

# Attendance Schemas
class AttendanceBase(BaseModel):
    usuario_id: int
    asamblea_id: int
    presente: bool

class AttendanceSchema(AttendanceBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True

# Address Schema
class AddressSchema(BaseModel):
    tipo_via: str
    numero_via: int
    numero_interseccion: Optional[str]
    barrio: str
    municipio: str
    departamento: str
    pais: str
    codigo_postal: str
    referencia: Optional[str]
    latitud: Optional[float]
    longitud: Optional[float]
    manzana: Optional[str]
    torre: Optional[str]
    apartamento: Optional[str]
    casa: Optional[str]


class CondominiumBase(BaseModel):
    name: str
    address: str
    legal_representative_id: int
    built_area: float


class OwnerBase(BaseModel):
    user_id: int
    condominium_id: int

class OwnerSchema(OwnerBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True

class CondominiumSchema(CondominiumBase):
    id: int
    owners: Optional[List[OwnerSchema]] = []
    units: Optional[List[UnitSchema]] = []
    assemblies: Optional[List[AssemblySchema]] = []

    class Config:
        orm_mode = True
        from_attributes = True


