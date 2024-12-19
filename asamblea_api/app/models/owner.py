from sqlalchemy import (Column, Integer, ForeignKey)
from sqlalchemy.orm import relationship

from app.core.database import Base

class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    condominium_id = Column(Integer, ForeignKey("condominiums.id"))

    user = relationship("User", back_populates="owner")
    condominium = relationship("Condominium", back_populates="owner")
    unit = relationship("Unit", back_populates="owner")
    attendances = relationship("Attendance", back_populates="owner")
    representations = relationship("Representation", back_populates="owner")
    attorney = relationship("Attorney", back_populates="owner")

