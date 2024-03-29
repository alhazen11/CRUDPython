"""add photo to user, delete timestamp

Revision ID: c6f3ba4ac904
Revises: 8678f7f75bf8
Create Date: 2019-10-21 14:35:38.503986

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c6f3ba4ac904'
down_revision = '8678f7f75bf8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('photo', sa.String(length=128), nullable=True))
    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'created_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('created_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('users', sa.Column('updated_at', mysql.DATETIME(), nullable=True))
    op.drop_column('users', 'photo')
    # ### end Alembic commands ###
