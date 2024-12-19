from sqlalchemy.orm import Session

from app.core.errors.exceptions import BadRequestException, TechnicalException
from app.core.logger import logger
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def find_all(self):
        return self.db.query(User).all()

    def create_user(self, user: UserCreate):
        db_user = User(full_name=user.full_name,
                       email=user.email,
                       hashed_password=user.password,
                       whatsapp=user.whatsapp,
                       phone=user.phone,
                       needs_assistance=user.needs_assistance)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        logger.info(f'User {user.full_name} created')
        return db_user

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter_by(email=email).first()

    def get_user_by_id(self, id: str):
        return self.db.query(User).filter_by(id=id).first()

    def update_user(self, user_f: User, user_update: UserUpdate) -> User:
        if not user_f:
            raise ValueError("The user instance is invalid.")

        # Update only the fields present in the request
        for key, value in user_update.dict(exclude_unset=True).items():
            setattr(user_f, key, value)

        try:
            # Commit the changes
            self.db.commit()
            # Refresh the instance to get the latest state
            self.db.refresh(user_f)
        except Exception as e:
            self.db.rollback()
            raise RuntimeError(f"Failed to update user: {e}")

        # Log the update
        logger.info(f"User {user_f.id} updated with fields: {user_update.dict(exclude_unset=True)}")
        return user_f

    def delete_user(self, email: str):
        try:
            user = self.db.query(User).filter(User.email == email).first()
            if not user:
                logger.info(f"{email} User not found")
                pass
            self.db.delete(user)
            self.db.commit()
            self.db.refresh(User)
            logger.info(f"User {user.id} deleted")
        except Exception as e:
            self.db.rollback()
            raise TechnicalException(detail=str(e))
