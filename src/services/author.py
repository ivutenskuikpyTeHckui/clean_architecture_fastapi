from src.schemas.author import AuthorSchemaAdd, AuthorSchemaDelete, AuthorSchemaUpdate

from src.utils.repository import AbstractRepository


class AuthorService:
    def __init__(self, author_repo: AbstractRepository):
        self.author_repo: AbstractRepository = author_repo()

    async def add_one(self, author: AuthorSchemaAdd):
        authors_dict = author.model_dump()
        author_id = await self.author_repo.add_one(authors_dict)
        return author_id
    
    async def get_all(self):
        authors = await self.author_repo.get_all()
        return authors
    
    async def delete_one(self, author_id: AuthorSchemaDelete):
        author_id = author_id.model_dump()["id"]
        author = await self.author_repo.delete_one(author_id)
        return author
    
    async def update_one(self, author: AuthorSchemaUpdate):
        author_dict = author.model_dump()
        author_id = await self.author_repo.update_one(author_dict)
        return author_id