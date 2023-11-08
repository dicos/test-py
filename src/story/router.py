from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated

from src.story.repository import story_repository
from src.exceptions import NotFound
from src.auth.utils import get_user_by_token
from src.story.schemas import CreateStoryRequest, CreateResponse
from src.user.models import User
from src.utils import jsonResp


router = APIRouter()

@router.post(
    '/create',
    response_model=CreateResponse,
    summary='Создание истории',
)
async def create(
        request: CreateStoryRequest, current_user: Annotated[User, Depends(get_user_by_token)]
    ) -> CreateResponse:
    '''
    ## Добавление истории.
    '''
    story_id = story_repository.create_story(user=current_user, text=request.text)
    return CreateResponse(id=story_id)


@router.post(
    '/{id}/view',
    response_model=CreateResponse,
    summary='Создаем пометку о просмотре истории'
)
async def view(id: int, current_user: Annotated[User, Depends(get_user_by_token)]):
    '''
    ## просмотр истории
    '''
    try:
        view_id = story_repository.view_story(user=current_user, story_id=id)
    except NotFound as e:
        return jsonResp.error(str(e), 404)

    return CreateResponse(id=view_id)

@router.get('/{username}/feed', summary='Не сделано')
async def feed():
    '''
    ## Получить истории пользователя.
    '''
    # @TODO: Реализовать функционал получения истории