import logging

from starlette.exceptions import HTTPException as StarletteHTTPException

from fastapi.exceptions import RequestValidationError
from fastapi import Request, status
from fastapi.responses import ORJSONResponse

from src.utils.exceptions import BaseAppException


logger = logging.getLogger("app")


async def app_exception_handler(request: Request, exc: BaseAppException) -> ORJSONResponse:
    logger.error(f"Application error: {exc.message}", exc_info=True)
    return ORJSONResponse(
        status_code=exc.status_code,
        content={
            "error_description": exc.message,
        }
    )


async def http_exception_handler(request: Request, exc: StarletteHTTPException) -> ORJSONResponse:
    return ORJSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError) -> ORJSONResponse:
    return ORJSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": exc.errors(), "body": exc.body}
    )
