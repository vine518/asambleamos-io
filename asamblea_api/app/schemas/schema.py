from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from enum import Enum

# Enums
class DocumentType(str, Enum):
    CC = "CC"
    TI = "TI"
    CE = "CE"
    NIT = "NIT"

class UserType(str, Enum):
    PROPIETARIO = "propietario"
    ADMINISTRADOR = "administrador"
    APODERADO = "apoderado"

class State(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    CANCELED = "canceled"

class AddressType(str, Enum):
    STREET = "Street"
    AVENUE = "Avenue"
    ROAD = "Road"
    CIRCLE = "Circle"
    LANE = "Lane"
    BOULEVARD = "Boulevard"
    DRIVE = "Drive"
    WAY = "Way"

# Schemas
class User(BaseModel):
    id: Optional[int]
    full_name: str = Field(..., alias="fullName")
    document_type: DocumentType = Field(..., alias="documentType")
    document_number: str = Field(..., alias="documentNumber")
    telephone: str
    email: EmailStr
    password: Optional[str]
    user_type: UserType = Field(..., alias="userType")
    needs_assistance: Optional[bool] = Field(False, alias="needsAssistance")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class Person(BaseModel):
    id: Optional[int]
    name: str
    document: str
    document_type: DocumentType = Field(..., alias="documentType")
    email: EmailStr
    phone: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class Property(BaseModel):
    id: Optional[int]
    address: str
    owners: List[Person]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class Coproperty(BaseModel):
    id: Optional[int]
    name: str
    address: str
    legal_representative_id: Optional[int] = Field(None, alias="legalRepresentativeId")
    constructed_area: Optional[float] = Field(None, alias="constructedArea")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class RealEstateUnit(BaseModel):
    id: Optional[int]
    type: str
    number: str
    constructed_area: float = Field(..., alias="constructedArea")
    coefficient: float
    owner_id: int = Field(..., alias="ownerId")
    coproperty_id: int = Field(..., alias="copropertyId")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class Assembly(BaseModel):
    id: Optional[int]
    name: str
    date: str
    coproperty_id: int = Field(..., alias="copropertyId")
    state: str
    description: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class Attendance(BaseModel):
    user_id: int = Field(..., alias="userId")
    assembly_id: int = Field(..., alias="assemblyId")
    attended: bool

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class Voting(BaseModel):
    id: Optional[int]
    question: str
    options: List[str]
    assembly_id: int = Field(..., alias="assemblyId")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class Vote(BaseModel):
    user_id: int = Field(..., alias="userId")
    voting_id: int = Field(..., alias="votingId")
    option: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class Booking(BaseModel):
    id: Optional[int]
    user_id: int = Field(..., alias="userId")
    property_id: int = Field(..., alias="propertyId")
    start_date: str = Field(..., alias="startDate")
    end_date: str = Field(..., alias="endDate")
    state: State

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class Notification(BaseModel):
    type: str
    message: str
    recipients: List[str]
    status: Optional[str]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
