"""leader del city

Revision ID: 348fb6ee31d5
Revises: 5a4acf6106c7
Create Date: 2018-08-19 16:18:04.523606

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '348fb6ee31d5'
down_revision = '5a4acf6106c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('leader', 'city')
    op.drop_constraint('phone_ibfk_1', 'phone', type_='foreignkey')
    op.create_foreign_key(None, 'phone', 'Qa', ['qa_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'phone', type_='foreignkey')
    op.create_foreign_key('phone_ibfk_1', 'phone', 'qa', ['qa_id'], ['id'])
    op.add_column('leader', sa.Column('city', mysql.VARCHAR(length=256), nullable=True))
    # ### end Alembic commands ###
