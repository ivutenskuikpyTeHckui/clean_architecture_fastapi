from src.schemas.book import (
    BookSchemaAdd,
    BookSchemaDelete,
    BookSchemaUpdate,
    AuthorForBookSchema,
)

from src.utils.uow import AbstractUnitOfWork


class BookService:
    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow

    async def add_one(self, book: BookSchemaAdd, author_ids: AuthorForBookSchema):
        kwargs = author_ids.model_dump()
        book_dict = book.model_dump()
        async with self.uow as uow:
            book_id = await uow.books.add_one(book_dict, **kwargs)
            return book_id

    async def get_all(self):
        async with self.uow as uow:
            books = await uow.books.get_all()
            return books

    async def delete_one(self, book_id: BookSchemaDelete):
        book_id = book_id.model_dump()["id"]
        async with self.uow as uow:
            book = await uow.books.delete_one(book_id)
            return book

    async def update_one(self, book: BookSchemaUpdate):
        book_dict = book.model_dump()
        async with self.uow as uow:
            book_id = await uow.books.update_one(book_dict)
            return book_id
