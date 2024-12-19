from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.user import UserAuth
from app.services.auth_service import AuthService
from app.services.user_service import UserService

router = APIRouter()


@router.post("/authenticate")
def login(
        user_auth: UserAuth,
        auth_service: AuthService = Depends(UserService)
):
    return {"access_token": auth_service.authenticate(user_auth), "token_type": "bearer"}


@router.post("/auth/login")
def login(auth_data: dict, db: Session = Depends(get_db)):
    # Authentication logic
    return {"token": "user_token"}


@router.post("/auth/validate-token")
def validate_token(auth_data: dict, db: Session = Depends(get_db)):
    # Token validation logic
    return {"message": "Token is valid"}
