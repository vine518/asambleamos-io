from app.core.auth.auth import create_access_token
from app.core.errors.exceptions import UnauthorizedException
from app.core.security.password_crypt import verify_password
from app.schemas.user import UserAuth
from app.services.user_service import UserService


class AuthService:

    def __init__(self, service: UserService):
        self.user_service = service

    def authenticate(self, user_auth: UserAuth):
        user = self.user_service.get_user_by_email(user_auth.email)
        if not user or not verify_password(user_auth.password, user.hashed_password):
            raise UnauthorizedException("Incorrect username or password")
        return create_access_token(data={"sub": str(user.id)})
