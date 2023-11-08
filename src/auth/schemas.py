from pydantic import BaseModel
from pydantic import field_validator

from src.validators import login_validate, pwd_validate, email_validate

class AuthRequest(BaseModel):
    username: str
    password: str

    @field_validator('username')
    @classmethod
    def check_username(cls, username: str) -> str:
        if login_validate(username):
            return username
        raise ValueError('invalid username')

    @field_validator('password')
    @classmethod
    def check_password(cls, password: str) -> str:
        if pwd_validate(password):
            return password
        raise ValueError('invalid password')


class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class LoginRequest(AuthRequest):
    email: str
    name: str

    @field_validator('email')
    @classmethod
    def check_email(cls, email: str) -> str:
        if email_validate(email):
            return email
        raise ValueError('invalid email')


class SignupResponse(BaseModel):
    status: str


