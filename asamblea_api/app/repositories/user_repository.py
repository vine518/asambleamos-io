from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

class UserRepository:
    def create_user(self, db: Session, user: UserCreate):
        db_user = User(name=user.name, email=user.email, hashed_password=user.password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def get_user_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()
