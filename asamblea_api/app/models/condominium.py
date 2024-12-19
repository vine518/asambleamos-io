from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.core.database import Base


class Condominium(Base):
    __tablename__ = "condominiums"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    legal_representative_id = Column(Integer, ForeignKey("users.id"))
    built_area = Column(Float, nullable=False)

    owner = relationship("Owner", back_populates="condominium")
    unit = relationship("Unit", back_populates="condominium")
    assembly = relationship("Assembly", back_populates="condominium")
