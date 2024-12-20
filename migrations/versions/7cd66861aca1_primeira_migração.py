"""Primeira migração

Revision ID: 7cd66861aca1
Revises: 
Create Date: 2024-12-16 01:22:52.596924

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7cd66861aca1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('registers', schema=None) as batch_op:
        batch_op.drop_index('email')
        batch_op.drop_index('id')

    op.drop_table('registers')
    op.drop_table('usuarios')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuarios',
    sa.Column('id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('email', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('senha', mysql.VARCHAR(length=50), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['registers.id'], name='usuarios_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('registers',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('DataCadastro', mysql.DATETIME(), nullable=False),
    sa.Column('nome', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('sobrenome', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('telefone', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('senha', mysql.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('registers', schema=None) as batch_op:
        batch_op.create_index('id', ['id'], unique=True)
        batch_op.create_index('email', ['email'], unique=True)

    # ### end Alembic commands ###
