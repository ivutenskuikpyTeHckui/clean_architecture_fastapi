from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.models.book import Book
from src.models.author import Author
from src.utils.repository import SQLAlchemyRepository
from src.db.database import async_session_maker




class BookRepository(SQLAlchemyRepository):
    model = Book

    async def add_one(self, data:dict, **kwargs) -> int:
        author_ids = kwargs.get("author_ids")
        print(author_ids, "hhi")
        if author_ids is None:
            return await super().add_one(data)
        else:
            async with async_session_maker() as session:
                book = self.model(**data)
                query = select(Author).where(Author.id.in_(author_ids))
                result = await session.execute(query)
                authors = result.scalars().all()
                book.authors.extend(authors)
                session.add(book)
                await session.commit()
                return book.id
    
    async def get_all(self):
        async with async_session_maker() as session:
            query = (
                select(
                    self.model
                ).options(
                    selectinload(Book.authors),
                )
            )
            books = await session.scalars(query)
            return list(books)
