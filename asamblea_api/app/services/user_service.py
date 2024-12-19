from fastapi import HTTPException, status, Depends

from app.core.database import get_db
from app.core.errors.exceptions import BusinessException
from app.core.logger import logger
from app.core.security.password_crypt import hash_password
from app.models import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserResponse, UserUpdate


class UserService:

    def __init__(self, user_repository: UserRepository = Depends(get_db)):
        self.user_repository = user_repository

    def create_user(self, user: UserCreate) -> UserResponse:
        # Logging para depuración
        logger.debug(f"Attempting to create user: {user.full_name} with email: {user.email}")

        # Verificar si el email ya está registrado
        existing_user = self.user_repository.get_user_by_email(user.email)
        if existing_user:
            logger.error(f"Email {user.email} is already registered.")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )

        user.password = hash_password(user.password)

        # Crear el usuario en el repositorio
        created_user = self.user_repository.create_user(user)

        # Devolver un modelo de respuesta compatible con Pydantic
        return UserResponse.from_orm(created_user)

    def update_user(self,email: str, user_update: UserUpdate) -> UserResponse:
        user_f = self.get_user_by_email(email)
        return self.user_repository.update_user(user_f, user_update)

    def get_user_by_email(self, email: str) -> User:
        # Obtener el usuario por email
        user = self.user_repository.get_user_by_email(email)
        if not user:
            logger.warning(f"User with email {email} not found.")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )

        # Devolver el modelo de respuesta
        return user

    def find_all(self) -> [UserResponse]:
        # Obtener el usuario por email
        users = self.user_repository.find_all()
        # Devolver el modelo de respuesta
        return [UserResponse.from_orm(user) for user in users]

    def get_user_by_id(self, id: str) -> UserResponse:
        # Obtener el usuario por email
        user = self.user_repository.get_user_by_id(id)
        if not user:
            logger.warning(f"User with id {id} not found.")
            raise BusinessException(
                code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )

        # Devolver el modelo de respuesta
        return UserResponse.from_orm(user)

    def disable_user(self, email: str):
        self.user_repository.delete_user(email)
