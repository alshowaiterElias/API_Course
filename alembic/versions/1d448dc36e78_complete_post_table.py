"""complete post table

Revision ID: 1d448dc36e78
Revises: 74cfb8da1369
Create Date: 2023-06-01 11:32:13.965084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d448dc36e78'
down_revision = '74cfb8da1369'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('Posts',
                  sa.Column('published', sa.Boolean(),
                            nullable=False, server_default='True'),
                  )
    op.add_column('Posts',
                  sa.Column('create_at', sa.TIMESTAMP(timezone=True),
                            nullable=False, server_default=sa.text("now()")),
                  )
    pass


def downgrade() -> None:
    op.drop_column('Posts', 'published')
    op.drop_column('Posts', 'create_at')
    pass
