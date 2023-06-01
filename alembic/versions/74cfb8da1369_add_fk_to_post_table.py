"""add FK to post table

Revision ID: 74cfb8da1369
Revises: ec4e2a60c448
Create Date: 2023-06-01 11:26:17.889648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74cfb8da1369'
down_revision = 'ec4e2a60c448'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('Posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('Posts_Users_FK', 'Posts', 'Users', [
                          'owner_id'], ['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('Posts_Users_FK', 'Posts')
    op.drop_column('Posts', 'owner_id')
    pass
