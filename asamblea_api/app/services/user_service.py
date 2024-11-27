from sqlalchemy.orm import Session

from app.core.logger import logger
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, db: Session, user: UserCreate):
        logger.debug(f"User: {user.name} Role: {user.email}")
        existing_user = self.user_repository.get_user_by_email(db, user.email)
        if existing_user:
            raise ValueError("Email already registered")
        return self.user_repository.create_user(db, user)

    def get_user_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()
