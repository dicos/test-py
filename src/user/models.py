from sqlalchemy import *
from ..models import BaseModel
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime

class User(BaseModel):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    name = Column(String)
    login = Column(String, unique=True)
    password = Column(String)
    last_seen = Column(DateTime)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    updated_at = Column(DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)
    # @TODO: реализовать связи
    
    @hybrid_property
    def is_online(self):
        if self.last_seen is None:
            return False
            
        return self.last_seen >= datetime.now()