"""add update_date in comment model

Revision ID: 06
Revises: 05
Create Date: 2023-06-02 20:35:42.894015

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06'
down_revision = '05'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment_post', sa.Column('date_update', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment_post', 'date_update')
    # ### end Alembic commands ###
