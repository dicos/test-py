import src.auth.schemas as AuthSchema
from src.user.repository import UserRepository

user_repository = UserRepository()
    
def login(request: AuthSchema.AuthRequest) -> dict:
    user = user_repository.find_by_login("login")
    # @TODO: реализовать функционал
    pass

def signup(request: AuthSchema.AuthRequest) -> dict:
    # @TODO: реализовать функционал
    pass