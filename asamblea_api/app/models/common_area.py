from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models import Condominium


class CommonArea(Base):
    __tablename__ = "common_areas"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255))
    condominium_id = Column(Integer, ForeignKey("condominiums.id", ondelete="CASCADE"), nullable=False)

    condominium = relationship("Condominium", back_populates="common_areas")
    bookings = relationship("Booking", back_populates="common_area")
