from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models import Person


class AccessLog(Base):
    __tablename__ = "access_logs"
    id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey("persons.id", ondelete="CASCADE"), nullable=False)
    area_name = Column(String(255), nullable=False)
    access_time = Column(TIMESTAMP, default=datetime.utcnow)

    person = relationship("Person", back_populates="access_logs")
