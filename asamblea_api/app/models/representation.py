from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class Representation(Base):
    __tablename__ = "representations"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("owners.id"))
    attorney_id = Column(Integer, ForeignKey("attorneys.id"))
    assembly_id = Column(Integer, ForeignKey("assemblies.id"))

    owner = relationship("Owner", back_populates="representations")
    attorney = relationship("Attorney", back_populates="representations")
    assembly = relationship("Assembly", back_populates="representations")
