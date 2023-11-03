from fastapi import APIRouter

router = APIRouter()

@router.post('/create')
async def create():
    '''
    ## Добавление поста.
    '''
    # @TODO: Реализовать функционал добавления истории

@router.post('/{id}/view')
async def view():
    '''
    ## Лайкнуть пост.
    '''
    # @TODO: Реализовать функционал просмотра истории

@router.get('/{username}/feed')
async def feed():
    '''
    ## Получить истории пользователя.
    '''
    # @TODO: Реализовать функционал получения истории