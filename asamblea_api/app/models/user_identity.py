from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint

from app.core.database import Base


class UserIdentity(Base):
    __tablename__ = "user_identities"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    provider_id = Column(Integer, ForeignKey("identity_providers.id", ondelete="CASCADE"), nullable=False)
    external_id = Column(String(255), nullable=False)

    __table_args__ = (UniqueConstraint("user_id", "provider_id", "external_id", name="uq_user_provider_external"),)
