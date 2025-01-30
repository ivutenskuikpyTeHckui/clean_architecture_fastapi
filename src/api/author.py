from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import auth_service
from src.schemas.author import AuthorSchemaAdd, AuthorSchemaDelete
from src.services.author import AuthorService


router = APIRouter(
    prefix="/authors",
    tags=["Authors"]
)

@router.post("")
async def add_one(
    author: AuthorSchemaAdd,
    author_service: Annotated[AuthorService, Depends(auth_service)],
):
    author_id = await author_service.add_one(author)
    return {"author_id": author_id}

@router.get("")
async def get_all(
    author_service: Annotated[AuthorService, Depends(auth_service)],
):
    authors = await author_service.get_all()
    return authors

@router.delete("")
async def delete_one(
    author_service: Annotated[AuthorService, Depends(auth_service)],
    author_id: AuthorSchemaDelete,
):
    author = await author_service.delete_one(author_id)
    return author