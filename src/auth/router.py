import src.auth.schemas as AuthSchema
from fastapi import APIRouter
from dotenv import load_dotenv
from src.exceptions import NotFound, AlreadyExists
from src.utils import jsonResp

load_dotenv('.env')
router = APIRouter()

@router.post('/login')
async def login(request: AuthSchema.AuthRequest):
    '''
    ## Авторизация пользователя.
    '''
    try:
        # @TODO: Реализовать функционал авторизации
        pass
    except NotFound as e:
        return jsonResp.error(str(e), 404)
    
@router.post('/signup')
async def signup(request: AuthSchema.AuthRequest):
    '''
    ## Регистрация пользователя.
    '''
    try:
        # @TODO: Реализовать функционал регистрации
        pass
    except AlreadyExists as e:
        return jsonResp.error(str(e), 403)
    

@router.post('/code',)
async def code():
    '''
    ## Отправка кода.
    '''
    # @TODO: Реализовать функционал отправки
    pass

@router.post('/code/check', tags=["Auth"])
async def checkCode():
    '''
    ## Проверка кода верификации.
    '''
    # @TODO: Реализовать функционал проверки учитывая кол-во попыток = 3
    pass