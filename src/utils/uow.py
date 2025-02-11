from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.author import AuthorRepository
from src.repositories.book import BookRepository


class AbstractUnitOfWork(ABC):
    authors: AuthorRepository
    books: BookRepository

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, traceback):
        if exc_type:
            await self.rollback()
        else:
            await self.commit()
        await self.session.close()

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError
    

class SQLAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def __aenter__(self):
        self.authors = AuthorRepository(self.session)
        self.books = BookRepository(self.session)
        return self

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()