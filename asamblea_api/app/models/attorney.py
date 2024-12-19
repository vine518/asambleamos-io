from sqlalchemy import (Column, Integer, ForeignKey)
from sqlalchemy.orm import relationship

from app.core.database import Base


class Attorney(Base):
    __tablename__ = "attorneys"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    owner_id = Column(Integer, ForeignKey("owners.id"))
    attendances_id = Column(Integer, ForeignKey("attendances.id"))
    votes_id = Column(Integer, ForeignKey("votes.id"))

    user = relationship("User", back_populates="attorney")
    owner = relationship("Owner", back_populates="attorney")
    attendances = relationship("Attendance", back_populates="attorney")
    votes = relationship("Vote", back_populates="attorney")
    representations = relationship("Representation", back_populates="attorney")
