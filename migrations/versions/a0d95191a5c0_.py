"""empty message

Revision ID: a0d95191a5c0
Revises: 4994f94014b5
Create Date: 2024-02-23 18:49:45.470611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0d95191a5c0'
down_revision = '4994f94014b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('globalset',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('timezonename', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('globalset')
    # ### end Alembic commands ###