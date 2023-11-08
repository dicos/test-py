from fastapi import HTTPException
from starlette import status


class NotFound(BaseException): ...

class IncorrectFields(BaseException): ...

class AlreadyExists(BaseException): ...

class Forbidden(BaseException): ...


credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)