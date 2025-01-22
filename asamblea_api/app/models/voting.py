from enum import Enum

from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class VotingState(Enum):
    OPEN = "open"
    CLOSED = "closed"


class Voting(Base):
    __tablename__ = "votings"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255), nullable=False)
    assembly_id = Column(Integer, ForeignKey("assemblies.id", ondelete="CASCADE"), nullable=False)
    state = Column(String(50), default="open")
    result = Column(String(255))

    assembly = relationship("Assembly", back_populates="votings")
    voting_questions = relationship("VotingQuestion", back_populates="voting")
