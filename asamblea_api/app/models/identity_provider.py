from sqlalchemy import Column, Integer, String, UniqueConstraint

from app.core.database import Base


class IdentityProvider(Base):
    __tablename__ = "identity_providers"
    id = Column(Integer, primary_key=True, index=True)
    provider_name = Column(String(255), nullable=False)
    provider_url = Column(String(255), nullable=False)

    __table_args__ = (UniqueConstraint("provider_name", name="uq_provider_name"),)
