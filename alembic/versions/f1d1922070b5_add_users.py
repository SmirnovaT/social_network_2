"""add_users

Revision ID: f1d1922070b5
Revises: 
Create Date: 2023-02-03 18:01:38.612260

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'f1d1922070b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String),
        sa.Column('username', sa.String),
        sa.Column('first_name', sa.String),
        sa.Column('last_name', sa.String),
        sa.Column('password', sa.String)

    )


def downgrade() -> None:
    op.drop_table('users')
