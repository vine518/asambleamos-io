from sqlalchemy import Column, Integer, String, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models import Person


class Condominium(Base):
    __tablename__ = "condominiums"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    legal_representative_id = Column(Integer, ForeignKey("persons.id", ondelete="SET NULL"))
    built_area = Column(Float, nullable=False)

    legal_representative = relationship("Person", back_populates="condominiums")
    assemblies = relationship("Assembly", back_populates="condominium")
    units = relationship("Unit", back_populates="condominium")
    owners = relationship("Owner", back_populates="condominium")
    common_areas = relationship("CommonArea", back_populates="condominium")
    expenses = relationship("Expense", back_populates="condominium")

    __table_args__ = (UniqueConstraint("name", "address", name="uq_condominium_name_address"),)


