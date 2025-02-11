from src.schemas.author import AuthorSchemaAdd, AuthorSchemaDelete, AuthorSchemaUpdate

from src.utils.uow import AbstractUnitOfWork


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
            return authors

    async def delete_one(self, author_id: AuthorSchemaDelete):
        author_id = author_id.model_dump()["id"]
        async with self.uow as uow:
            author = await uow.authors.delete_one(author_id)
            return author

    async def update_one(self, author: AuthorSchemaUpdate):
        author_dict = author.model_dump()
        async with self.uow as uow:
            author_id = await uow.authors.update_one(author_dict)
            return author_id
