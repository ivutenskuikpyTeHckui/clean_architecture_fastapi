from typing import List, TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.database import Base
from src.models.association_author_book import Association_Author_Book
if TYPE_CHECKING:
    from src.models.author import Author


class Book(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    authors: Mapped[List["Author"]] = relationship(secondary=Association_Author_Book.__tablename__,
                                                   back_populates="books")
