import src.user.models as UserModel
from src.models import SessionLocal

class UserRepository:
    def __init__(self):
        self.db = SessionLocal()
        
    def find_by_login(self) -> UserModel.User:
        pass