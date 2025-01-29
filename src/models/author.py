from typing import List, TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.database import Base
from src.models.association_author_book import Association_Author_Book
if TYPE_CHECKING:
    from src.models.book import Book


class Author(Base):
    __tablename__ = "author"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    books: Mapped[List["Book"]] = relationship(secondary=Association_Author_Book.__tablename__, 
                                                   back_populates="authors"
                                                   )