from sqlalchemy import *
from ..models import BaseModel
from datetime import datetime

class Posts(BaseModel):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))
    code = Column(String, unique=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    updated_at = Column(DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)
    
    # @TODO: реализовать связи

class PostComments(BaseModel):
    __tablename__ = 'post_comments'
    
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id', ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey('users.id'))
    parent_id = Column(Integer, nullable=True)
    text = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    updated_at = Column(DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)
    
    # @TODO: реализовать связи