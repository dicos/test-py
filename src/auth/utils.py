from datetime import timedelta, datetime
from typing import Annotated

from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from pydantic import BaseModel
from starlette import status

from src.user.repository import user_repository
from src.auth.constants import SECRET_KEY, ALGORITHM
from src.exceptions import NotFound, credentials_exception
from src.models import oauth2_scheme, pwd_context
from src.user.models import User


async def get_user_by_token(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = user_repository.find_by_login(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


class TokenData(BaseModel):
    username: str | None = None


def authenticate_user(username: str, password: str) -> User:
    user = user_repository.find_by_login(username)
    if not user_repository.verify_password(password, user.password):
        raise NotFound
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
