from enum import Enum

from sqlalchemy import (Column, Integer, String, Boolean, Enum as SqlEnum, DateTime)
from sqlalchemy.orm import relationship

from app.core.database import Base


class UserRole(Enum):
    OWNER = "owner"
    ATTORNEY = "attorney"
    ASSISTANT = "assistant"
    ADMIN = "admin"


# Models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    whatsapp = Column(String, nullable=True)
    phone = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    needs_assistance = Column(Boolean, nullable=False, default=False)

    hashed_password = Column(String, nullable=False)
    attendance_token = Column(String, nullable=True)
    token_expiration = Column(DateTime, nullable=True)
    cookie = Column(String, nullable=True)
    role = Column(SqlEnum(UserRole), default=UserRole.OWNER, nullable=False)

    owner = relationship("Owner", back_populates="user")
    attorney = relationship("Attorney", back_populates="user")
    attendances = relationship("Attendance", back_populates="user")
    votes = relationship("Vote", back_populates="user")
