from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.errors.exceptions import BadRequestException
from app.core.security.password_crypt import hash_password
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserResponse, UserCreate
from app.services.user_service import UserService

router = APIRouter()

user_service = UserService(UserRepository())


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        password = hash_password(user.password)
        user.password = password
        return user_service.create_user(db, user)
    except ValueError as e:
        raise BadRequestException(detail=str(e))
