from sqlalchemy import (Column, Integer, String, ForeignKey, UniqueConstraint)
from sqlalchemy.orm import relationship

from app.core.database import Base


class Agenda(Base):
    __tablename__ = "agendas"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255), nullable=False)
    assembly_id = Column(Integer, ForeignKey("assemblies.id", ondelete="CASCADE"), nullable=False)
    order = Column(Integer, nullable=False)

    assembly = relationship("Assembly", back_populates="agendas")
    agenda_items = relationship("AgendaItem", back_populates="agenda")

    __table_args__ = (UniqueConstraint("description", "assembly_id", name="uq_agenda_description_assembly"),)
