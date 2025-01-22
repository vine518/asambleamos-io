from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models import Owner, Unit


class Representation(Base):
    __tablename__ = "representations"
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("owners.id", ondelete="CASCADE"), nullable=False)
    attorney_id = Column(Integer, ForeignKey("attorneys.id", ondelete="SET NULL"))
    assembly_id = Column(Integer, ForeignKey("assemblies.id", ondelete="CASCADE"), nullable=False)
    unit_id = Column(Integer, ForeignKey("units.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("Owner", back_populates="representations")
    attorneys = relationship("Attorney", back_populates="representations")
    assembly = relationship("Assembly", back_populates="representations")
    unit = relationship("Unit", back_populates="representations")
    attendances = relationship("Attendance", back_populates="representation")


