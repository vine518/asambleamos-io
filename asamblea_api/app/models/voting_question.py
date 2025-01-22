from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from app.core.database import Base


# Models for Voting Questions and Votes
class VotingQuestion(Base):
    __tablename__ = "voting_questions"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255), nullable=False)
    agenda_item_id = Column(Integer, ForeignKey("agenda_items.id", ondelete="CASCADE"), nullable=False)
    voting_id = Column(Integer, ForeignKey("votings.id", ondelete="CASCADE"), nullable=False)

    agenda_item = relationship("AgendaItem", back_populates="voting_questions")
    voting = relationship("Voting", back_populates="voting_questions")
    votes = relationship("Vote", back_populates="question")

    __table_args__ = (UniqueConstraint("description", "voting_id", name="uq_question_description_voting"),)
