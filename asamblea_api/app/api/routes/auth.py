from datetime import timedelta

from fastapi import APIRouter

from app.core.auth.auth import create_access_token
from app.core.database import get_db
from app.core.errors.exceptions import UnauthorizedException
from app.core.security.password_crypt import verify_password
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserAuth
from app.services.user_service import UserService

router = APIRouter()

userService = UserService(UserRepository())


@router.post("/token")
def login(user_auth: UserAuth):
    user = userService.get_user_by_email(user_auth.email)
    if not user or not verify_password(user_auth.password, user.hashed_password):
        raise UnauthorizedException("Incorrect username or password")
    access_token = create_access_token(
        data={"sub": str(user.id)},
        expires_delta=timedelta(minutes=30)
    )
    return {"access_token": access_token, "token_type": "bearer"}

