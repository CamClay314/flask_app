"""Initialize database schema

Revision ID: 92121cf24ab9
Revises: 8dc9d7bf84cf
Create Date: 2024-12-05 23:43:08.104481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92121cf24ab9'
down_revision = '8dc9d7bf84cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('guest_entry', schema=None) as batch_op:
        batch_op.add_column(sa.Column('message', sa.Text(), nullable=False))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.drop_column('location')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('guest_entry', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location', sa.VARCHAR(length=120), nullable=False))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)
        batch_op.drop_column('created_at')
        batch_op.drop_column('message')

    # ### end Alembic commands ###