from src.models.author import Author
from src.utils.repository import SQLAlchemyRepository


class AuthorRepository(SQLAlchemyRepository):
    model = Author

    