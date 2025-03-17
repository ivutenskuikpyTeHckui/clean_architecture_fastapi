import logging
from fastapi import Request
from fastapi.responses import ORJSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class ExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as exc:
            return ORJSONResponse(
                status_code=500,
                content={
                    "error": "Internal Server Error",
                    "error_description": "Упс... Что-то пошло не так, попробуйте позже."
                }
            )
