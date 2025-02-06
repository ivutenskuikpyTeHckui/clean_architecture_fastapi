from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.author import AuthorRepository
from src.repositories.book import BookRepository

from src.services.author import AuthorService
from src.services.book import BookService

from src.db.database import get_async_session


def book_service(session: Annotated[AsyncSession, Depends(get_async_session)]) -> BookService:
    repository = BookRepository(session)
    return BookService(repository)

def auth_service(session: Annotated[AsyncSession, Depends(get_async_session)]):
    repository = AuthorRepository(session)
    return AuthorService(repository)
