"""auto-vote

Revision ID: f06744eea8d6
Revises: 1d448dc36e78
Create Date: 2023-06-01 11:43:34.467578

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f06744eea8d6'
down_revision = '1d448dc36e78'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['Posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    op.add_column('Posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()'), nullable=False))
    op.drop_column('Posts', 'create_at')
    op.add_column('Users', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()'), nullable=False))
    op.drop_column('Users', 'create_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('create_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False))
    op.drop_column('Users', 'created_at')
    op.add_column('Posts', sa.Column('create_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False))
    op.drop_column('Posts', 'created_at')
    op.drop_table('Votes')
    # ### end Alembic commands ###
