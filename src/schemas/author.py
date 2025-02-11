from pydantic import BaseModel


class AuthorSchemaBase(BaseModel):
    pass


class AuthorSchemaAdd(AuthorSchemaBase):
    name: str


class AuthorSchemaDelete(AuthorSchemaBase):
    id: int


class AuthorSchemaUpdate(AuthorSchemaBase):
    id: int
    name: str
