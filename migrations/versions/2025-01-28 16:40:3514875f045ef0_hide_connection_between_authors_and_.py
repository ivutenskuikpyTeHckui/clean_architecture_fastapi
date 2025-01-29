"""hide connection between authors and books

Revision ID: 14875f045ef0
Revises: 6ee0d9d88a9c
Create Date: 2025-01-28 16:40:35.655304

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14875f045ef0'
down_revision: Union[str, None] = '6ee0d9d88a9c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association_author_book')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('association_author_book',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('book_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('author_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], name='association_author_book_author_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], name='association_author_book_book_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='association_author_book_pkey'),
    sa.UniqueConstraint('author_id', 'book_id', name='idx_product_category')
    )
    # ### end Alembic commands ###
