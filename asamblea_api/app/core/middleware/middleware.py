from datetime import time

from fastapi import Request
from prometheus_fastapi_instrumentator import Instrumentator
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logger import logger
from app.schemas.error_response import ErrorResponse


class ExceptionHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as exc:
            logger.error(f"Unhandled error: {exc}", exc_info=True)
            return ErrorResponse(code=500, message=f'Internal server error: {exc}')


class ExecutionTimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        response.headers["X-Execution-Time"] = str(duration)
        return response


def setup_metrics(app):
    Instrumentator().instrument(app).expose(app)
