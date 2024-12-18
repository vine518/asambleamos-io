from http.client import HTTPException

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependecies import get_service
from app.core.errors.exceptions import BadRequestException
from app.core.security.password_crypt import hash_password
from app.models.user import User
from app.schemas.user import UserResponse, UserCreate, UserBase
from app.schemas.vote import UserSchema
from app.services.user_service import UserService

router = APIRouter()


@router.post("/", response_model=UserResponse)
def create_user(
        user: UserCreate,
        user_service: UserService = Depends(get_service)
):
    try:
        password = hash_password(user.password)
        user.password = password

        return user_service.create_user(user)
    except ValueError as e:
        raise BadRequestException(detail=str(e))


@router.get("/all")
def get_all_users(
        user_service: UserService = Depends(get_service)
):
    try:
        return user_service.find_all()
    except ValueError as e:
        raise BadRequestException(detail=str(e))


@router.get("/{id}", response_model=UserResponse)
def get_user(id: str, user_service: UserService = Depends(get_service)):
    try:
        return user_service.get_user_by_id(id)
    except ValueError as e:
        raise BadRequestException(detail=str(e))

@router.post("/users", response_model=UserSchema)
def register_user(user: UserSchema, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    return new_user


@router.get("/users/{id}", response_model=UserSchema)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/users/{id}", response_model=UserSchema)
def update_user(id: int, user: UserSchema, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    return db_user


@router.delete("/users/{id}")
def disable_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": f"User {id} disabled"}
