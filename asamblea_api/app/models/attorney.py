from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models import Person


class Attorney(Base):
    __tablename__ = "attorneys"
    id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey("persons.id", ondelete="CASCADE"), nullable=False)
    owner_id = Column(Integer, ForeignKey("owners.id", ondelete="CASCADE"), nullable=False)

    person = relationship("Person", back_populates="attorneys")
    owners = relationship("Owner", back_populates="attorneys")
    representations = relationship("Representation", back_populates="attorneys")


