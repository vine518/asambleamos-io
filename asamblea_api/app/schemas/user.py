from pydantic import BaseModel, EmailStr

from app.core.database import Base, engine


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

    class Config:
        orm_mode = True


Base.metadata.create_all(bind=engine)
