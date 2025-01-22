from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.core.database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255), nullable=False)
    amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default="now()")
    condominium_id = Column(Integer, ForeignKey("condominiums.id", ondelete="CASCADE"), nullable=False)

    condominium = relationship("Condominium", back_populates="expenses")
