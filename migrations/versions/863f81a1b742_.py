"""empty message

Revision ID: 863f81a1b742
Revises: a0d95191a5c0
Create Date: 2024-02-26 17:25:06.957539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '863f81a1b742'
down_revision = 'a0d95191a5c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('globalset', schema=None) as batch_op:
        batch_op.add_column(sa.Column('settingid', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('setting', sa.String(), nullable=False))
        batch_op.drop_column('timezonename')
        batch_op.drop_column('id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('globalset', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
        batch_op.add_column(sa.Column('timezonename', sa.VARCHAR(), autoincrement=False, nullable=False))
        batch_op.drop_column('setting')
        batch_op.drop_column('settingid')

    # ### end Alembic commands ###