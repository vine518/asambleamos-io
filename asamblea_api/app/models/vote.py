from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models import Unit


class Vote(Base):
    __tablename__ = "votes"
    id = Column(Integer, primary_key=True, index=True)
    unit_id = Column(Integer, ForeignKey("units.id", ondelete="CASCADE"), nullable=False)
    question_id = Column(Integer, ForeignKey("voting_questions.id", ondelete="CASCADE"), nullable=False)
    answer = Column(String(255), nullable=False)
    timestamp = Column(TIMESTAMP, default=datetime.utcnow)

    unit = relationship("Unit", back_populates="votes")
    question = relationship("VotingQuestion", back_populates="votes")


