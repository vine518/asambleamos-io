from app.core.errors.exceptions import UnauthorizedException
from app.core.settings import Settings, get_property
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

access_token_expire_minutes = get_property("ACCESS_TOKEN_EXPIRE_MINUTES")
jwt_secret_key = get_property("JWT_SECRET_KEY")
algorithm = get_property("ALGORITHM")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = access_token_expire_minutes or (datetime.now() + (expires_delta or timedelta(minutes=15)))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, jwt_secret_key, algorithm=algorithm)


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, jwt_secret_key, algorithms=[algorithm])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise UnauthorizedException("Invalid token")
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise UnauthorizedException("User not found")
        return user
    except JWTError:
        raise UnauthorizedException("Invalid token")


def check_role(required_role: str):
    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role != required_role:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return current_user
    return role_checker
