"""rename address

Revision ID: 38b806527534
Revises: 37fe9db7597a
Create Date: 2024-09-19 10:27:56.328436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38b806527534'
down_revision = '37fe9db7597a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###
