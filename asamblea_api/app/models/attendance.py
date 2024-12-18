from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.core.database import Base


class Attendance(Base):
    __tablename__ = "attendances"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    assembly_id = Column(Integer, ForeignKey("assemblies.id"))
    present = Column(Boolean, default=False)

    # Use string reference if User is not yet defined
    user = relationship("User", back_populates="attendances")
    assembly = relationship("Assembly", back_populates="attendances")
