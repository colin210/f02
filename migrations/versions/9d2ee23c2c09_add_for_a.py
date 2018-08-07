"""add for a

Revision ID: 9d2ee23c2c09
Revises: 83b9bf3d0d5e
Create Date: 2018-08-07 22:42:46.940680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d2ee23c2c09'
down_revision = '83b9bf3d0d5e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('phone', sa.Column('machine_owner', sa.String(length=128), nullable=True))
    op.drop_constraint('phone_ibfk_1', 'phone', type_='foreignkey')
    op.create_foreign_key(None, 'phone', 'Qa', ['qa_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'phone', type_='foreignkey')
    op.create_foreign_key('phone_ibfk_1', 'phone', 'qa', ['qa_id'], ['id'])
    op.drop_column('phone', 'machine_owner')
    # ### end Alembic commands ###
