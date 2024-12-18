from sqlalchemy import (Column, Integer, String, Boolean, Enum, DateTime, ForeignKey)
from sqlalchemy.orm import relationship, declarative_base

from app.core.database import Base


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

    owners = relationship("Owner", back_populates="users")
    attorneys = relationship("Attorney", back_populates="users")
    attendances = relationship("Attendance", back_populates="users")
    votes = relationship("Vote", back_populates="users")


class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    condominium_id = Column(Integer, ForeignKey("condominiums.id"))

    users = relationship("User", back_populates="owners")
    condominium = relationship("Condominium", back_populates="owners")
    units = relationship("Unit", back_populates="owners")
    attendances = relationship("Attendance", back_populates="owners")
    representations = relationship("Representation", back_populates="owners")


class Attorney(Base):
    __tablename__ = "attorneys"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    owner_id = Column(Integer, ForeignKey("owners.id"))

    users = relationship("User", back_populates="attorneys")
    owner = relationship("Owner", back_populates="attorney")
    attendances = relationship("Attendance", back_populates="attorney")
    votes = relationship("Vote", back_populates="attorney")
    representations = relationship("Representation", back_populates="attorney")

