from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import book_service
from src.schemas.book import BookSchemaAdd, AuthorForBookSchema, BookSchemaDelete
from src.services.book import BookService


router = APIRouter(
    prefix="/book",
    tags=["Book"],
)

@router.post("")
async def add_one(
    book: BookSchemaAdd,
    book_service: Annotated[BookService, Depends(book_service)],
    author_ids: AuthorForBookSchema = None,
):
    kwargs = author_ids.model_dump()
    book_id = await book_service.add_one(book, **kwargs)
    return {"book_id": book_id}


@router.get("")
async def get_all(
    book_service: Annotated[BookService, Depends(book_service)],
):
    books = await book_service.get_all()
    return books

@router.delete("")
async def delete_one(
    book_service: Annotated[BookService, Depends(book_service)],
    book_id: BookSchemaDelete,
):
    book = await book_service.delete_one(book_id)
    return book