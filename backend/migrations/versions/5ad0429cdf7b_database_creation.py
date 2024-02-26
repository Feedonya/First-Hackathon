"""git

Revision ID: 5ad0429cdf7b
Revises:
Create Date: 2024-02-24 16:05:19.875944

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ad0429cdf7b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('role',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('permissions', sa.JSON(), nullable=True),
                    sa.PrimaryKeyConstraint('id'))
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('role_id', sa.Integer(), nullable=True),
                    sa.Column('hashed_password', sa.String(), nullable=False),
                    sa.Column('is_active', sa.Boolean(), nullable=False, default=False),
                    sa.Column('is_superuser', sa.Boolean(), nullable=False, default=False),
                    sa.Column('is_verified', sa.Boolean(), nullable=False, default=False),
                    sa.ForeignKeyConstraint(['role_id'], ['role.id']),
                    sa.PrimaryKeyConstraint('id'))
    op.create_table('groups',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('owner_id', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id'))
    op.create_table('group_members',
                    sa.Column('group_id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['group_id'], ['groups.id']),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id']))
    op.create_table('organisations',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('admin_id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('full_name', sa.String(), nullable=False),
                    sa.Column('slug', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.ForeignKeyConstraint(['admin_id'], ['users.id']))
    op.create_table('course_categories',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('parent_id', sa.Integer(), nullable=True),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('desc', sa.String(), nullable=False),
                    sa.Column('slug', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id'))
    op.create_table('courses',
                    sa.Column('id', sa.Integer()),
                    sa.Column('owner_id', sa.Integer(), nullable=False),
                    sa.Column('category', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('is_open', sa.Boolean(), nullable=False, default=True),
                    sa.Column('sword', sa.Boolean(), nullable=True),
                    sa.Column('slug', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.ForeignKeyConstraint(['owner_id'], ['organisations.id']),
                    sa.ForeignKeyConstraint(['category'], ['course_categories.id']))
    op.create_table('tasks',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('course_id', sa.Integer(), nullable=True),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('max_grade', sa.Integer(), nullable=False, default=100),
                    sa.Column('slug', sa.String()),
                    sa.PrimaryKeyConstraint('id'),
                    sa.ForeignKeyConstraint(['course_id'], ['courses.id']))
    op.create_table('course_members',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('role', sa.Integer(), nullable=False),
                    sa.Column('course_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id']),
                    sa.ForeignKeyConstraint(['course_id'], ['courses.id']))
    op.create_table('attempts',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('number', sa.Integer(), nullable=False),
                    sa.Column('mark', sa.Float(), nullable=True),
                    sa.Column('mark_desc', sa.String(), nullable=True),
                    sa.Column('mark_teacher', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id']),
                    sa.PrimaryKeyConstraint('id'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    op.drop_table('roles')
    op.drop_table('attempts')
    op.drop_table('course_tasks')
    op.drop_table('course_categories')
    op.drop_table('course_members')
    op.drop_table('courses')
    op.drop_table('organisations')
    op.drop_table('groups')
    op.drop_table('group_members')
    pass
