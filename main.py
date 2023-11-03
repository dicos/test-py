from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from src import router

app = FastAPI(
    title="Test fork",
    description='Developed on FastAPI',
    version="1.0",
    contact={
        "name": "Farik Baratoff",
        "url": "https://t.me/farik_baratoff",
    }
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=['*'],
#     allow_credentials=True,
#     allow_methods=['*'],
#     allow_headers=['*'],
# )

app.include_router(router)

# @TODO: Реализовать мидлвару для обновления поле last_seen

# @TODO: Реализовать функционал очистки истории у которых created_at >= 24 hours