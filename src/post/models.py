from sqlalchemy import *
from src.common.log import loging_models
from ..models import BaseModel
from datetime import datetime

class Posts(BaseModel):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))
    code = Column(String, unique=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    updated_at = Column(DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)


class PostLikes(BaseModel):
    __tablename__ = 'post_likes'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id', ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey('users.id'))

class PostComments(BaseModel):
    __tablename__ = 'post_comments'
    
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id', ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey('users.id'))
    parent_id = Column(Integer, nullable=True)
    text = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    updated_at = Column(DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)
    

class PostCommentLikes(BaseModel):
    __tablename__ = 'post_comment_likes'

    id = Column(Integer, primary_key=True)
    comment_id = Column(Integer, ForeignKey('comment.id', ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey('users.id'))


loging_models(Posts, PostLikes, PostComments, PostCommentLikes)
