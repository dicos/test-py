from datetime import timedelta
from typing import Annotated

import src.auth.schemas as AuthSchema
from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from dotenv import load_dotenv

from src.auth.constants import ACCESS_TOKEN_EXPIRE
from src.auth.utils import authenticate_user, create_access_token
from src.exceptions import NotFound, AlreadyExists
from src.user.repository import user_repository
from src.utils import jsonResp

load_dotenv('.env')
router = APIRouter()


@router.post(
    '/login',
    response_model=AuthSchema.AuthResponse,
    summary='Авторизация пользователя',
    description='Авторизация пользователя по логину и паролю. Если авторизация прошла успешно, выдается jwt токен'
)
async def login(request: Annotated[OAuth2PasswordRequestForm, Depends()]):
    '''
    ## Авторизация пользователя.
    '''
    try:
        user = authenticate_user(request.username, request.password)
    except NotFound as e:
        return jsonResp.error(str(e), 404)
    access_token_expires = timedelta(seconds=ACCESS_TOKEN_EXPIRE)
    access_token = create_access_token(
        data={"sub": user.login}, expires_delta=access_token_expires
    )
    return AuthSchema.AuthResponse(access_token=access_token)

@router.post(
    '/signup',
    response_model=AuthSchema.SignupResponse,
    summary='Регистрация пользователя',
    description='Регистрация пользователя. Поля email и username уникальные. Если при регистрации какое-то поле уже'
                ' есть в базе данных, то регистрация невозможна.'
)
async def signup(request: AuthSchema.LoginRequest):
    '''
    ## Регистрация пользователя.
    '''

    try:
        user_repository.registration(
            email=request.email,
            name=request.name,
            username=request.username,
            password=request.password
        )
        return AuthSchema.SignupResponse(status='ok')
    except AlreadyExists as e:
        return jsonResp.error(str(e), 403)
    

@router.post('/code', summary='Не сделано')
async def code():
    '''
    ## Отправка кода.
    '''
    # @TODO: Реализовать функционал отправки
    pass

@router.post('/code/check', tags=["Auth"], summary='Не сделано')
async def checkCode():
    '''
    ## Проверка кода верификации.
    '''
    # @TODO: Реализовать функционал проверки учитывая кол-во попыток = 3
    pass