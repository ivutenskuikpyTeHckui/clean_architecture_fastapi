from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.models.book import Book
from src.models.author import Author
from src.utils.repository import SQLAlchemyRepository


class BookRepository(SQLAlchemyRepository):
    model = Book

    async def add_one(self, data: dict, **kwargs) -> int:
        author_ids = kwargs.get("author_ids")
        if author_ids is None:
            return await super().add_one(data)
        else:
            book = self.model(**data)
            query = select(Author).where(Author.id.in_(author_ids))
            result = await self.session.execute(query)
            authors = result.scalars().all()
            book.authors.extend(authors)
            self.session.add(book)
            return book.id

    async def get_all(self):
        query = (
            select(
                self.model
            ).options(
                selectinload(Book.authors),
            )
        )
        books = await self.session.scalars(query)
        return list(books)
