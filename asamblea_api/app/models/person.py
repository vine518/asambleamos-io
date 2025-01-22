from sqlalchemy import Column, Integer, String, Boolean, UniqueConstraint
from sqlalchemy.orm import relationship

from app.core.database import Base


class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), nullable=False)
    whatsapp = Column(String(50))
    phone = Column(String(50))
    email = Column(String(255), unique=True, nullable=False)
    needs_assistance = Column(Boolean, default=False)

    user = relationship("User", back_populates="person", uselist=False)
    access_logs = relationship("AccessLog", back_populates="person")
    owners = relationship("Owner", back_populates="person")
    notifications = relationship("Notification", back_populates="recipient")
    condominiums = relationship("Condominium", back_populates="legal_representative")
    bookings = relationship("Booking", back_populates="person")
    attorneys = relationship("Attorney", back_populates="person")

    __table_args__ = (UniqueConstraint("email", name="uq_person_email"),)
