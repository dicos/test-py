from fastapi import APIRouter

router = APIRouter()

@router.post('/create')
async def create():
    '''
    ## Добавление поста.
    '''
    # @TODO: Реализовать функционал добавления постов

@router.post('/{code}/like')
async def like():
    '''
    ## Лайкнуть пост.
    '''
    # @TODO: Реализовать функционал добавления лайка

@router.post('/{code}/comment')
async def comment():
    '''
    ## Добавление комментария.
    '''
    # @TODO: Реализовать функционал добавления комментария