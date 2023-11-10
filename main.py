import asyncio

from fastapi import FastAPI
from fastapi import Request, HTTPException
import uvicorn
# from fastapi.middleware.cors import CORSMiddleware
from src import router
from src.auth.utils import get_user_by_token_without_depends
from src.story.repository import story_repository
from src.user.repository import user_repository


async def periodic_tasks():
    sleep = 60 * 30  # 30 minutes
    while 1:
        story_repository.delete_old_stories()
        await asyncio.sleep(sleep)


app = FastAPI(
    title="Test fork",
    description='Developed on FastAPI',
    version="1.0",
    contact={
        "name": "Farik Baratoff",
        "url": "https://t.me/farik_baratoff",
    },
    on_startup=(periodic_tasks,)
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=['*'],
#     allow_credentials=True,
#     allow_methods=['*'],
#     allow_headers=['*'],
# )


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    if request.headers.get('authorization'):
        try:
            user = get_user_by_token_without_depends(request.headers['authorization'].split()[-1])
        except HTTPException as e:
            raise e
        else:
            if not user.is_online:
                user_repository.set_online(user)
    return response

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

# @TODO: Реализовать мидлвару для обновления поле last_seen

# @TODO: Реализовать функционал очистки истории у которых created_at >= 24 hours