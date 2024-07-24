"""empty message

Revision ID: a00510aa6ed1
Revises: 4f38f8e90268
Create Date: 2024-07-24 12:14:55.760921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a00510aa6ed1'
down_revision = '4f38f8e90268'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('libro', schema=None) as batch_op:
        batch_op.alter_column('precio',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=True)
        batch_op.alter_column('cantidad',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('libro', schema=None) as batch_op:
        batch_op.alter_column('cantidad',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('precio',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=False)

    # ### end Alembic commands ###