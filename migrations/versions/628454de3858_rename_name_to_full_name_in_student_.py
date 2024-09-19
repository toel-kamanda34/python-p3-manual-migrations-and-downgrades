"""Rename name to full_name in Student model

Revision ID: 628454de3858
Revises: b5f7c117ef13
Create Date: 2024-09-19 19:35:13.261038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '628454de3858'
down_revision = 'b5f7c117ef13'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='full_name')

def downgrade() -> None:
    op.alter_column('students', 'full_name', new_column_name='name')
