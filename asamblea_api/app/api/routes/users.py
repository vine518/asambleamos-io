from fastapi import APIRouter, Depends

from app.core.dependecies import get_service
from app.core.errors.exceptions import BadRequestException
from app.schemas.user import UserResponse, UserCreate, UserUpdate
from app.services.user_service import UserService

router = APIRouter()


@router.post("/", response_model=UserResponse)
def create_user(
        user: UserCreate,
        user_service: UserService = Depends(get_service)
):
    try:
        return user_service.create_user(user)
    except ValueError as e:
        raise BadRequestException(detail=str(e))


@router.get("/", response_model=list[UserResponse])
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


@router.put("/{email}", response_model=UserResponse)
def update_user(email: str, user: UserUpdate, user_service: UserService = Depends(get_service)):
    return UserResponse.from_orm(user_service.update_user(email, user))


@router.delete("/{email}")
def disable_user(email: str, user_service: UserService = Depends(get_service)):
    user_service.disable_user(email)
    return {"message": f"User {email} disabled"}
