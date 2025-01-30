from typing import List, Optional

from pydantic import BaseModel


class AuthorSchemaBase(BaseModel):
    pass

class AuthorSchemaAdd(AuthorSchemaBase):
    name: str

class AuthorSchemaDelete(AuthorSchemaBase):
    id: int

class AuthorSchemaUpdate(AuthorSchemaBase):
    id: Optional[int | None]
    name: Optional[str | None]