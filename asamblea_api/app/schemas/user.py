from enum import Enum

from pydantic import BaseModel, EmailStr

from app.core.database import Base, engine


class UserType(Enum):
    User = 'usuario'
    Representative = "apoderado"
    Owner = "propietario"
    Assistant = "asistente"
    Administrator = "administrador"


class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserAuth(BaseModel):
    email: EmailStr
    password: str


class UserResponse(UserBase):
    id: int


Base.metadata.create_all(bind=engine)
