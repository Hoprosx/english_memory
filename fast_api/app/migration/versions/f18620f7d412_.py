"""empty message

Revision ID: f18620f7d412
Revises: 
Create Date: 2024-03-30 20:03:37.751536

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f18620f7d412'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('english_words',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('russian_words',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(), nullable=False),
    sa.Column('eng_word_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['eng_word_id'], ['english_words.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('russian_words')
    op.drop_table('english_words')
    # ### end Alembic commands ###