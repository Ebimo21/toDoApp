"""empty message

Revision ID: 83eb4be3c691
Revises: 
Create Date: 2022-07-31 21:36:37.737347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83eb4be3c691'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('list', sa.Column('completed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('list', 'completed')
    # ### end Alembic commands ###