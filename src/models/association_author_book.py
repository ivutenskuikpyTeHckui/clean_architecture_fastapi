from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.db.database import Base


class Association_Author_Book(Base):
    __tablename__ = "association_author_book"
    __table_args__ = (
        UniqueConstraint(
            "author_id",
            "book_id",
            name="idx_product_category",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("book.id", ondelete="CASCADE"))
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id", ondelete="CASCADE"))
