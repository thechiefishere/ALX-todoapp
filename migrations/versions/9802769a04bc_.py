"""empty message

Revision ID: 9802769a04bc
Revises: 07003034afae
Create Date: 2022-08-11 16:44:31.208896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9802769a04bc'
down_revision = '07003034afae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('completed', sa.Boolean(), nullable=True))
    
    op.execute('UPDATE todo SET completed = False WHERE completed IS NULL;')
    
    op.alter_column('todo', 'completed', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todo', 'completed')
    # ### end Alembic commands ###
