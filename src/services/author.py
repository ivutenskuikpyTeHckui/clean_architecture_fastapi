from src.schemas.author import AuthorSchemaAdd, AuthorSchemaDelete, AuthorSchemaUpdate

from src.utils.uow import AbstractUnitOfWork

from src.utils.exceptions import (
    ResourceNotFoundException,
    InvalidIDException,
)


class AuthorService:
    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow

    async def add_one(self, author: AuthorSchemaAdd):
        authors_dict = author.model_dump()
        async with self.uow as uow:
            author_id = await uow.authors.add_one(authors_dict)
            return author_id

    async def get_all(self):
        async with self.uow as uow:
            authors = await uow.authors.get_all()
            if not authors:
                raise ResourceNotFoundException("Авторы не найдены.")
            return authors

    async def delete_one(self, author_id: AuthorSchemaDelete):
        author_id = author_id.model_dump()["id"]
        if author_id < 1:
            raise InvalidIDException(f"Переданное значение id {author_id} недопустимо. Оно должно быть больше 0.")
        async with self.uow as uow:
            author = await uow.authors.delete_one(author_id)
            if author is None:
                raise ResourceNotFoundException(f"Автор с id {author_id} не найден.")
            return author

    async def update_one(self, author: AuthorSchemaUpdate):
        author_dict = author.model_dump()
        if author_dict["id"] < 1:
            raise InvalidIDException(f"Переданное значение id {author_dict['id']} недопустимо. Оно должно быть больше 0.")
        async with self.uow as uow:
            author_id = await uow.authors.update_one(author_dict)
            return author_id
