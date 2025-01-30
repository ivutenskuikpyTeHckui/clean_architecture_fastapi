from src.schemas.book import (
    BookSchemaAdd, 
    BookSchemaDelete, 
    BookSchemaUpdate, 
    AuthorForBookSchema,
)

from src.utils.repository import AbstractRepository


class BookService:
    def __init__(self, book_repo: AbstractRepository):
        self.book_repo: AbstractRepository = book_repo()

    async def add_one(self, book: BookSchemaAdd, author_ids: AuthorForBookSchema):
        kwargs = author_ids.model_dump()
        book_dict = book.model_dump()
        book_id = await self.book_repo.add_one(book_dict, **kwargs)
        return book_id
    
    async def get_all(self):
        books = await self.book_repo.get_all()
        return books
    
    async def delete_one(self, book_id: BookSchemaDelete):
        book_id = book_id.model_dump()["id"]
        book = await self.book_repo.delete_one(book_id)
        return book

    async def update_one(self, book: BookSchemaUpdate):
        book_dict = book.model_dump()
        book_id = await self.book_repo.update_one(book_dict)
        return book_id