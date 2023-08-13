"""create_comments_on_post

Revision ID: 05
Revises: 04
Create Date: 2023-05-11 20:55:11.765630

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '05'
down_revision = '04'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment_post',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('date_create', sa.DateTime(), server_default='now()', nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('post', sa.Column('date_create', sa.DateTime(), server_default='now()', nullable=True))
    op.drop_column('post', 'date')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('date', postgresql.TIMESTAMP(), server_default=sa.text("'2023-04-19 22:31:09.400292'::timestamp without time zone"), autoincrement=False, nullable=True))
    op.drop_column('post', 'date_create')
    op.drop_table('comment_post')
    # ### end Alembic commands ###