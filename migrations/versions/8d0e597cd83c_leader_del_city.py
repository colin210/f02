"""leader del city

Revision ID: 8d0e597cd83c
Revises: 348fb6ee31d5
Create Date: 2018-08-19 16:18:26.158648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d0e597cd83c'
down_revision = '348fb6ee31d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('phone_ibfk_1', 'phone', type_='foreignkey')
    op.create_foreign_key(None, 'phone', 'Qa', ['qa_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'phone', type_='foreignkey')
    op.create_foreign_key('phone_ibfk_1', 'phone', 'qa', ['qa_id'], ['id'])
    # ### end Alembic commands ###
