from typing import List, Optional

from pydantic import BaseModel


class AuthorSchemaBase(BaseModel):
    pass

class AuthorSchemaAdd(AuthorSchemaBase):
    name: str

class AuthorSchemaDelete(AuthorSchemaBase):
    id: int