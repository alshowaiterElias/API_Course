"""add User Table

Revision ID: ec4e2a60c448
Revises: 6026b130ef54
Create Date: 2023-06-01 11:17:30.479049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec4e2a60c448'
down_revision = '6026b130ef54'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('Users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('create_at', sa.TIMESTAMP(timezone=True),
                              nullable=False, server_default=sa.text("now()")),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('Users')
