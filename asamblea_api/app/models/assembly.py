from enum import Enum

from sqlalchemy import Integer, String, Column, ForeignKey, TIMESTAMP
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
    name = Column(String(255), nullable=False)
    date = Column(TIMESTAMP, nullable=False)
    condominium_id = Column(Integer, ForeignKey("condominiums.id", ondelete="CASCADE"), nullable=False)
    state = Column(String(50), default="scheduled")

    attendances = relationship("Attendance", back_populates="assembly")
    condominium = relationship("Condominium", back_populates="assemblies")
    agendas = relationship("Agenda", back_populates="assembly")
    representations = relationship("Representation", back_populates="assembly")
    votings = relationship("Voting", back_populates="assembly")


