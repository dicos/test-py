"""add likes

Revision ID: 75ca8fc2a9f5
Revises: b898a2fc1fc2
Create Date: 2023-11-08 17:17:33.570895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75ca8fc2a9f5'
down_revision = 'b898a2fc1fc2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'post_likes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('post_id', sa.Integer, nullable=False),
        sa.Column('user_id', sa.Integer),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    )

    op.create_table(
        'post_comment_likes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('comment_id', sa.Integer, nullable=False),
        sa.Column('user_id', sa.Integer),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['comment_id'], ['post_comments.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    )


def downgrade() -> None:
    op.drop_table('post_likes')
    op.drop_table('post_comment_likes')
