"""add models and tables

Revision ID: 6cac4397d8d2
Revises: 
Create Date: 2023-08-07 12:02:12.367381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cac4397d8d2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_ingredients'))
    )
    op.create_table('soups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_soups'))
    )
    op.create_table('soup_ingredients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('soup_id', sa.Integer(), nullable=True),
    sa.Column('ingredient_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredients.id'], name=op.f('fk_soup_ingredients_ingredient_id_ingredients')),
    sa.ForeignKeyConstraint(['soup_id'], ['soups.id'], name=op.f('fk_soup_ingredients_soup_id_soups')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_soup_ingredients'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('soup_ingredients')
    op.drop_table('soups')
    op.drop_table('ingredients')
    # ### end Alembic commands ###
