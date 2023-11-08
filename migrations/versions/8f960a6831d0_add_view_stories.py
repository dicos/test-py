"""empty message

Revision ID: 8f960a6831d0
Revises: 75ca8fc2a9f5
Create Date: 2023-11-08 21:27:48.498705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f960a6831d0'
down_revision = '75ca8fc2a9f5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'story_views',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('story_id', sa.Integer, nullable=False),
        sa.Column('user_id', sa.Integer),
        sa.Column('created_at', sa.DateTime),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['story_id'], ['stories.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    )


def downgrade() -> None:
    op.drop_table('story_views')
