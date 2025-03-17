from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from src.api.exception_handlers import (
    app_exception_handler,
    http_exception_handler,
    validation_exception_handler,
)
from src.api.router import all_routers


from src.utils.exceptions import BaseAppException
from src.utils.middleware import ExceptionMiddleware


app = FastAPI(title="Books and Authors", debug=True)


"""
Здесь регистрируется обработчик для всех исключений, производных от BaseAppException.
Это означает, что если в бизнес‑логике выбрасывается любое пользовательское исключение,
оно будет перехвачено и обработано обработчиком app_exception_handler.
"""
app.add_exception_handler(BaseAppException, app_exception_handler)


"""
Миддвар для обработки непойманных ошибок.
"""
# app.add_middleware(ExceptionMiddleware)

app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)


for router in all_routers:
    app.include_router(router)