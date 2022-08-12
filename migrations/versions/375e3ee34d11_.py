"""empty message

Revision ID: 375e3ee34d11
Revises: 9802769a04bc
Create Date: 2022-08-12 08:28:52.245574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '375e3ee34d11'
down_revision = '9802769a04bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todolist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('todo', sa.Column('todolist_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'todo', 'todolist', ['todolist_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todo', type_='foreignkey')
    op.drop_column('todo', 'todolist_id')
    op.drop_table('todolist')
    # ### end Alembic commands ###