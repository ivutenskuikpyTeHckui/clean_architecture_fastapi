from typing import List

from pydantic import BaseModel


class BookSchemaBase(BaseModel):
    pass


# Схемы для добавлние книг с учетом связи МТМ
class BookSchemaAdd(BookSchemaBase):
    title: str


class AuthorForBookSchema(BaseModel):
    author_ids: List[int]


# Схема для удаления книги по Id
class BookSchemaDelete(BookSchemaBase):
    id: int


class BookSchemaUpdate(BookSchemaBase):
    id: int
    title: str
