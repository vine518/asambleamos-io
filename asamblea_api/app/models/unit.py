from enum import Enum

from sqlalchemy import Column, Integer, String, Float, ForeignKey, UniqueConstraint, Enum as SQLEnum
from sqlalchemy.orm import relationship

from app.core.database import Base


class UnitType(SQLEnum):
    APARTMENT = "apartment"
    PARKING = "parking"
    HOUSE = "house"
    COMMERCIAL_UNIT = "commercial_unit"


class Unit(Base):
    __tablename__ = "units"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(SQLEnum(name="type"), default=UnitType.APARTMENT, nullable=False)
    number = Column(String(12), nullable=False)
    built_area = Column(Float, nullable=False)
    coefficient = Column(Integer, nullable=False)
    owner_id = Column(Integer, ForeignKey("owners.id", ondelete="SET NULL"))
    condominium_id = Column(Integer, ForeignKey("condominiums.id", ondelete="CASCADE"))

    owner = relationship("Owner", back_populates="units")
    condominium = relationship("Condominium", back_populates="units")
    representations = relationship("Representation", back_populates="unit")
    votes = relationship("Vote", back_populates="unit")

    __table_args__ = (UniqueConstraint("number", "condominium_id", name="uq_unit_number_condominium"),)
