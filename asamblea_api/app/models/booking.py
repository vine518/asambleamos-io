from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models import CommonArea, Person


class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    common_area_id = Column(Integer, ForeignKey("common_areas.id", ondelete="CASCADE"), nullable=False)
    person_id = Column(Integer, ForeignKey("persons.id", ondelete="CASCADE"), nullable=False)
    start_time = Column(TIMESTAMP, nullable=False)
    end_time = Column(TIMESTAMP, nullable=False)

    common_area = relationship("CommonArea", back_populates="bookings")
    person = relationship("Person", back_populates="bookings")


