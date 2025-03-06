from fastapi import FastAPI
from core.auth.router import auth_router
from core.chat.router import chat


def create_api() -> FastAPI:
    api = FastAPI()
    api.include_router(auth_router, prefix="", tags=["Authentication"])
    api.include_router(chat, prefix="/chat", tags=["Chat"])

    return api
