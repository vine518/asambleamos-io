from enum import Enum

from sqlalchemy import Column, Integer, ForeignKey, Enum as SQLEnum, String, Float
from sqlalchemy.orm import relationship

from app.core.database import Base


class UnitType(str, Enum):
    APARTMENT = "apartment"
    PARKING = "parking"
    HOUSE = "house"
    COMMERCIAL_UNIT = "commercial_unit"

class Unit(Base):
    __tablename__ = "units"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(SQLEnum(UnitType), nullable=False)
    number = Column(String(12), nullable=False)
    built_area = Column(Float(30), nullable=False)
    coefficient = Column(Integer, nullable=False)
    owner_id = Column(Integer, ForeignKey("owners.id"))
    condominium_id = Column(Integer, ForeignKey("condominiums.id"))

    owner = relationship("Owner", back_populates="unit")
    condominium = relationship("Condominium", back_populates="unit")