# import src.user.models as UserModel  # такого класса не существует
from datetime import datetime, timedelta

from src.models import SessionLocal, pwd_context
from sqlalchemy.exc import NoResultFound
from src.user.models import User
from src.exceptions import NotFound, AlreadyExists

class UserRepository:
    def __init__(self):
        self.db = SessionLocal()
        
    def find_by_login(self, username: str) -> User:
        try:
            return self.db.query(User).filter(User.login==username).one()
        except NoResultFound:
            raise NotFound

    def registration(self, *, email: str, name: str, username: str, password: str) -> User:
        if self.db.query(User).filter(User.login==username or User.email==email).scalar():
            raise AlreadyExists('user already exists')
        user = User(
            email=email,
            name=name,
            login=username,
            password=pwd_context.hash(password)
        )
        self.db.add(user)
        self.db.commit()
        return user

    def verify_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    def set_online(self, user:User):
        user.last_seen = datetime.now() + timedelta(minutes=3)
        self.db.add(user)
        self.db.commit()

user_repository = UserRepository()
