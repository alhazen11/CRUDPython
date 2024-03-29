"""add sensor, sensor_data, etc..

Revision ID: 526599a0a109
Revises: 8bb31ccf278c
Create Date: 2019-10-12 14:15:59.440104

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '526599a0a109'
down_revision = '8bb31ccf278c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sensors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('notifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('device_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.String(length=255), nullable=True),
    sa.Column('read', sa.Boolean(), nullable=True),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['device_id'], ['devices.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sensors_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('device_id', sa.Integer(), nullable=True),
    sa.Column('sensor_id', sa.Integer(), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['device_id'], ['devices.id'], ),
    sa.ForeignKeyConstraint(['sensor_id'], ['sensors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('power_expenses', sa.Column('title', sa.String(length=120), nullable=True))
    op.add_column('switches', sa.Column('duration', sa.Integer(), nullable=True))
    op.add_column('switches', sa.Column('status', sa.Boolean(), nullable=True))
    op.add_column('switches', sa.Column('triggered_by', sa.String(length=120), nullable=True))
    op.drop_column('usage_histories', 'duration')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usage_histories', sa.Column('duration', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_column('switches', 'triggered_by')
    op.drop_column('switches', 'status')
    op.drop_column('switches', 'duration')
    op.drop_column('power_expenses', 'title')
    op.drop_table('sensors_data')
    op.drop_table('notifications')
    op.drop_table('sensors')
    # ### end Alembic commands ###
