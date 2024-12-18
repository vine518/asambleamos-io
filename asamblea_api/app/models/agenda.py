from sqlalchemy import (Column, Integer, String, ForeignKey)
from sqlalchemy.orm import relationship

from app.core.database import Base


class Agenda(Base):
    __tablename__ = "agendas"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    assembly_id = Column(Integer, ForeignKey("assemblies.id"))
    order = Column(Integer, nullable=False)

    assembly = relationship("Assembly", back_populates="agendas")
    questions = relationship("VotingQuestion", back_populates="agenda")
