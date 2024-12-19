from fastapi import HTTPException


class NotFoundException(HTTPException):
    def __init__(self, detail: str = "Resource not found"):
        super().__init__(status_code=404, detail=detail)


class UnauthorizedException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=401, detail=detail or "Unauthorized")


class BadRequestException(HTTPException):
    def __init__(self, detail: str = "Bad request"):
        super().__init__(status_code=400, detail=detail)


class AssemblyBaseException(HTTPException):
    def __init__(self, detail: str = "", code: int = 500):
        super().__init__(status_code=code, detail=detail)


class BusinessException(AssemblyBaseException):
    def __init__(self, detail: str = "Business exception", code: int = 422):
        super().__init__(detail=detail, code=code)


class TechnicalException(AssemblyBaseException):
    def __init__(self, detail: str = "Technical exception", code: int = 500):
        super().__init__(detail=detail, code=code)
