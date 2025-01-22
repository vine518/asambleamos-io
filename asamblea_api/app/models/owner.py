from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from app.core.database import Base


class Owner(Base):
    __tablename__ = "owners"
    id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey("persons.id", ondelete="CASCADE"), nullable=False)
    condominium_id = Column(Integer, ForeignKey("condominiums.id", ondelete="CASCADE"), nullable=False)

    attorneys = relationship("Attorney", back_populates="owners")
    person = relationship("Person", back_populates="owners")
    condominium = relationship("Condominium", back_populates="owners")
    units = relationship("Unit", back_populates="owner")
    representations = relationship("Representation", back_populates="owner")

    __table_args__ = (UniqueConstraint("person_id", "condominium_id", name="uq_owner_person_condominium"),)
