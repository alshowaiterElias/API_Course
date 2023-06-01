"""create post table

Revision ID: 27f9bd0bfd66
Revises: 
Create Date: 2023-06-01 10:54:57.357164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27f9bd0bfd66'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('Posts', sa.Column(
        'id', sa.Integer, nullable=False, primary_key=True), sa.Column(
        'title', sa.String, nullable=False))


def downgrade() -> None:
    op.drop_table('Posts')
