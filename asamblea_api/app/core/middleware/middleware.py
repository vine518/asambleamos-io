from datetime import time
from fastapi import Request
from prometheus_fastapi_instrumentator import Instrumentator
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from app.core.logger import logger


class ExceptionHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as exc:
            logger.error(f"Unhandled error: {exc}", exc_info=True)
            return JSONResponse(
                status_code=500, content={"detail": "Internal server error"}
            )


class ExecutionTimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        response.headers["X-Execution-Time"] = str(duration)
        return response


def setup_metrics(app):
    Instrumentator().instrument(app).expose(app)
