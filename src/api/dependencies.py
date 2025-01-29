from src.repositories.author import AuthorRepository
from src.repositories.book import BookRepository
from src.services.author import AuthorService
from src.services.book import BookService


def book_service():
    return BookService(BookRepository)

def auth_service():
    return AuthorService(AuthorRepository)
