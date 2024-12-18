from fastapi import HTTPException, status, Depends

from app.core.database import get_db
from app.core.logger import logger
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserResponse


class UserService:

    def __init__(self, user_repository: UserRepository = Depends(get_db)):
        self.user_repository = user_repository

    def create_user(self, user: UserCreate) -> UserResponse:
        # Logging para depuración
        logger.debug(f"Attempting to create user: {user.name} with email: {user.email}")

        # Verificar si el email ya está registrado
        existing_user = self.user_repository.get_user_by_email(user.email)
        if existing_user:
            logger.error(f"Email {user.email} is already registered.")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )

        # Crear el usuario en el repositorio
        created_user = self.user_repository.create_user(user)

        # Devolver un modelo de respuesta compatible con Pydantic
        return UserResponse.from_orm(created_user)

    def get_user_by_email(self, email: str) -> UserResponse:
        # Obtener el usuario por email
        user = self.user_repository.get_user_by_email(email)
        if not user:
            logger.warning(f"User with email {email} not found.")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )

        # Devolver el modelo de respuesta
        return UserResponse.from_orm(user)

    def find_all(self) -> [UserResponse]:
        # Obtener el usuario por email
        users = self.user_repository.find_all()
        # Devolver el modelo de respuesta
        return UserResponse.from_orm(users)

    def get_user_by_id(self, id: str) -> UserResponse:
        # Obtener el usuario por email
        user = self.user_repository.get_user_by_id(id)
        if not user:
            logger.warning(f"User with id {id} not found.")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )

        # Devolver el modelo de respuesta
        return UserResponse.from_orm(user)
