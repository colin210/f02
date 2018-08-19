"""leader city

Revision ID: a7545b155624
Revises: 5ae9612fd61b
Create Date: 2018-08-19 16:02:46.458541

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a7545b155624'
down_revision = '5ae9612fd61b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('leader')
    op.drop_constraint('phone_ibfk_1', 'phone', type_='foreignkey')
    op.create_foreign_key(None, 'phone', 'Qa', ['qa_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'phone', type_='foreignkey')
    op.create_foreign_key('phone_ibfk_1', 'phone', 'qa', ['qa_id'], ['id'])
    op.create_table('leader',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('group_name', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('name', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('age', mysql.VARCHAR(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###