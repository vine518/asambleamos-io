from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService


##
## Entry point for dependencies for underlying layers. We need to keep a new approach for dependency injection
##
def get_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(UserRepository(db))
