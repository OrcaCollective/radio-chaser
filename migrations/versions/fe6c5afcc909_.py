"""empty message

Revision ID: fe6c5afcc909
Revises: 
Create Date: 2021-04-12 14:52:31.977802

"""
from datetime import datetime

from alembic import op
from environs import Env
import sqlalchemy as sa

from radio_chaser.extensions import bcrypt

env = Env()
env.read_env()


# revision identifiers, used by Alembic.
revision = 'fe6c5afcc909'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    users = op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.LargeBinary(length=128), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=True),
    sa.Column('last_name', sa.String(length=30), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###
    # Custom command for adding an initial user
    op.bulk_insert(users, [{
        "username": "techbloc",
        "password": bcrypt.generate_password_hash(env.str("ADMIN_PASSWORD")),
        "active": True,
        "is_admin": True,
        "created_at": datetime.now()
    }])


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles')
    op.drop_table('users')
    # ### end Alembic commands ###
