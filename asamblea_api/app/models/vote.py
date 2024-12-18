from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship

from app.core.database import Base


class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("voting_questions.id"))
    answer = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="votes")
    question = relationship("VotingQuestion", back_populates="votes")
