from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated

import src.post.schemas as PostSchema
from src.auth.utils import get_user_by_token
from src.exceptions import NotFound, AlreadyExists
from src.post.repository import post_repository
from src.user.models import User
from src.utils import jsonResp

router = APIRouter()

@router.post(
    '/create',
    response_model=PostSchema.CreateResponse,
    summary='Создание поста'
)
async def create(request: PostSchema.CreatePostRequest, current_user: Annotated[User, Depends(get_user_by_token)]):
    '''
    ## Добавление поста.
    '''
    try:
        post_id = post_repository.create_post(user=current_user, code=request.code)
    except AlreadyExists as e:
        return jsonResp.error(str(e), 403)
    return PostSchema.CreateResponse(id=post_id)

@router.post(
    '/{code}/like',
    response_model=PostSchema.CreateResponse,
    summary='Лайк поста'
)
async def like(code: str, current_user: Annotated[User, Depends(get_user_by_token)]):
    '''
    ## Лайкнуть пост.
    '''
    try:
        like_id = post_repository.add_like(user=current_user, code=code)
    except NotFound as e:
        return jsonResp.error(str(e), 404)
    return PostSchema.CreateResponse(id=like_id)

@router.post(
    '/{code}/comment',
    response_model=PostSchema.CreateResponse,
    summary='Добавление коммента к посту',
    description='Параметр parent_id не обязательный, вместо него может быть null'
)
async def comment(
        code: str, request: PostSchema.CreateComment, current_user: Annotated[User, Depends(get_user_by_token)]
    ):
    '''
    ## Добавление комментария.
    '''
    try:
        comment_id = post_repository.add_comment(
            user=current_user, code=code, text=request.text, parent_id=request.parent_id
        )
    except NotFound as e:
        return jsonResp.error(str(e), 404)
    return PostSchema.CreateResponse(id=comment_id)

@router.post(
    '{username}/feed',
    response_model=list[PostSchema.FeedResponseItem],
    summary='Список постов пользователя',
    description='Возвращает список из кода поста, кол-ва лайков и 2 последних комментариев'
)
async def feed(username: str) -> list[PostSchema.FeedResponseItem]:
    '''
    ## Реализовать возможность получения постов пользователя, с выводом последних 2х комментариев (будем считать как топ комменты), лайкнут ли пост
    '''
    posts = post_repository.get_post_list(username=username)
    results = []
    for code, likes, comment_1, comment_2 in posts:
        results.append(PostSchema.FeedResponseItem(code=code, likes=likes, comment_1=comment_1, comment_2=comment_2))
    return results