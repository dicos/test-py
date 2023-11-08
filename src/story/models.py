from sqlalchemy import *
from ..models import BaseModel
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime

class Stories(BaseModel):
    __tablename__ = 'stories'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    text = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    updated_at = Column(DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)


class StoryViews(BaseModel):
    __tablename__ = "story_views"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    story_id = Column(Integer, ForeignKey('stories.id'))
    created_at = Column(DateTime(timezone=True), default=datetime.now)