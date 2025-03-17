

class BaseAppException(Exception):
    """
    Базовое исключение для приложения.
    """
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class ResourceNotFoundException(BaseAppException):
    """
    Исключение, выбрасываемое, когда запрошенный ресурс не найден.
    """
    def __init__(self, message: str):
        super().__init__(message, status_code=404)


class InvalidIDException(BaseAppException):
    """Исключение, выбрасываемое, когда переданное значение id меньше 1."""
    def __init__(self, message: str):
        super().__init__(message, status_code=400)
