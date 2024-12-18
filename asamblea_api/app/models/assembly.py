from enum import Enum

from sqlalchemy import Integer, String, DateTime, Column, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship

from app.core.database import Base


class AssemblyState(Enum):
    SCHEDULED = "scheduled"
    STARTED = "started"
    SUSPENDED = "suspended"
    FINISHED = "finished"


class Assembly(Base):
    __tablename__ = "assemblies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    condominium_id = Column(Integer, ForeignKey("condominiums.id"))
    state = Column(SQLEnum(AssemblyState), nullable=False)

    condominium = relationship("Condominium", back_populates="assemblies")
    agendas = relationship("Agenda", back_populates="assembly")
    votings = relationship("Voting", back_populates="assembly")
    representations = relationship("Representation", back_populates="assembly")