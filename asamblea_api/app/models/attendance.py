from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models import Representation


class Attendance(Base):
    __tablename__ = "attendances"
    id = Column(Integer, primary_key=True, index=True)
    representation_id = Column(Integer, ForeignKey("representations.id", ondelete="CASCADE"), nullable=False)
    assembly_id = Column(Integer, ForeignKey("assemblies.id", ondelete="CASCADE"), nullable=False)
    present = Column(Boolean, default=False)

    representation = relationship("Representation", back_populates="attendances")
    assembly = relationship("Assembly", back_populates="attendances")


