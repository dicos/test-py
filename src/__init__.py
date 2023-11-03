from fastapi import APIRouter
from src.auth.router import router as auth_router
from src.post.router import router as post_router
from src.story.router import router as story_router

router = APIRouter(prefix='/api/v1')

router.include_router(auth_router, prefix='/auth', tags=['Auth'])
router.include_router(post_router, prefix='/posts', tags=['Post'])
router.include_router(story_router, prefix='/stories', tags=['Story'])