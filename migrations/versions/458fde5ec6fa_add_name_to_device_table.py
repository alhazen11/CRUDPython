"""add name to device table

Revision ID: 458fde5ec6fa
Revises: 5f7eab46c2c2
Create Date: 2019-10-15 09:07:33.093977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '458fde5ec6fa'
down_revision = '5f7eab46c2c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('devices', sa.Column('name', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('devices', 'name')
    # ### end Alembic commands ###
