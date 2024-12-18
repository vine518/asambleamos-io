from enum import Enum

from sqlalchemy import Integer, Column, String, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship

from app.core.database import Base


class VotingState(Enum):
    OPEN = "open"
    CLOSED = "closed"


class Voting(Base):
    __tablename__ = "votings"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    assembly_id = Column(Integer, ForeignKey("assemblies.id"))
    state = Column(SQLEnum(VotingState), nullable=False)
    result = Column(String, nullable=True)

    assembly = relationship("Assembly", back_populates="votings")
