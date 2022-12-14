"""empty message

Revision ID: 3666e68f6477
Revises: 8df9354b2b87
Create Date: 2022-09-06 11:04:05.496389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3666e68f6477'
down_revision = '8df9354b2b87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kakeibo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('budget', sa.Integer(), nullable=True),
    sa.Column('item', sa.String(), nullable=True),
    sa.Column('cost', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('kakeibo')
    # ### end Alembic commands ###
