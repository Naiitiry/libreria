"""empty message

Revision ID: 29c994fc381a
Revises: 
Create Date: 2024-08-01 23:13:17.655520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29c994fc381a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('autor', schema=None) as batch_op:
        batch_op.add_column(sa.Column('imagen_autor', sa.String(), nullable=True))

    with op.batch_alter_table('libro', schema=None) as batch_op:
        batch_op.add_column(sa.Column('imagen_url', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('libro', schema=None) as batch_op:
        batch_op.drop_column('imagen_url')

    with op.batch_alter_table('autor', schema=None) as batch_op:
        batch_op.drop_column('imagen_autor')

    # ### end Alembic commands ###