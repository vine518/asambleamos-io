from enum import Enum

from sqlalchemy import (Column, Integer, String, ForeignKey, TIMESTAMP)
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models import Person, Role


class UserRole(Enum):
    User = 'usuario'
    Representative = "apoderado"
    Owner = "propietario"
    Assistant = "asistente"
    Administrator = "administrador"


# Models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey("persons.id", ondelete="CASCADE"), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    attendance_token = Column(String(255))
    token_expiration = Column(TIMESTAMP)
    cookie = Column(String(255))
    role_id = Column(Integer, ForeignKey("roles.id", ondelete="SET NULL"))

    person = relationship("Person", back_populates="user")
    role = relationship("Role", back_populates="user")