from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class VotingQuestion(Base):
    __tablename__ = "voting_questions"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    agenda_id = Column(Integer, ForeignKey("agendas.id"))

    agenda = relationship("Agenda", back_populates="questions")
    votes = relationship("Vote", back_populates="question")
