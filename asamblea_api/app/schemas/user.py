from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr

from app.core.database import Base, engine


class UserType(Enum):
    User = 'usuario'
    Representative = "apoderado"
    Owner = "propietario"
    Assistant = "asistente"
    Administrator = "administrador"


class UserBase(BaseModel):
    full_name: Optional[str]
    whatsapp: Optional[str]
    phone: Optional[str]
    email: Optional[EmailStr]
    needs_assistance: Optional[bool]
    role: Optional[UserType]

    class Config:
        orm_mode = True
        from_attributes = True


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    class Config:
        orm_mode = True
        from_attributes = True


class UserAuth(BaseModel):
    password: str
    attendance_token: str
    token_expiration: str
    cookie: str


class UserResponse(UserBase):
    id: int
