"""add a new column for post

Revision ID: 6026b130ef54
Revises: 27f9bd0bfd66
Create Date: 2023-06-01 11:06:54.760810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6026b130ef54'
down_revision = '27f9bd0bfd66'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('Posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('Posts', 'content')
    pass
