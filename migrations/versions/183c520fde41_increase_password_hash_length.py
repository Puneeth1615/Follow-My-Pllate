"""Increase password_hash length

Revision ID: 183c520fde41
Revises: ef1bc2df0e00
Create Date: 2025-07-17 00:52:21.992539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '183c520fde41'
down_revision = 'ef1bc2df0e00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=255),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)

    # ### end Alembic commands ###
