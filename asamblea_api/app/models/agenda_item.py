from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from app.core.database import Base


class AgendaItem(Base):
    __tablename__ = "agenda_items"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255), nullable=False)
    agenda_id = Column(Integer, ForeignKey("agendas.id", ondelete="CASCADE"), nullable=False)
    order = Column(Integer, nullable=False)

    agenda = relationship("Agenda", back_populates="agenda_items")
    voting_questions = relationship("VotingQuestion", back_populates="agenda_item")

    __table_args__ = (UniqueConstraint("description", "agenda_id", name="uq_agenda_item_description"),)
