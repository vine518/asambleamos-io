from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate

class UserRepository:

    def __init__(self):
        self.db = Depends(get_db)

    def create_user(self, user: UserCreate):
        db_user = User(name=user.name, email=user.email, hashed_password=user.password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()
