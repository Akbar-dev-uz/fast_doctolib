from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.routers import api_router
from app.db.session import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # код при запуске
    init_db()
    print("✅ База инициализирована")
    yield
    # код при завершении
    print("🛑 Приложение завершает работу")


app = FastAPI(lifespan=lifespan, version="1.0.0",)

app.include_router(api_router, prefix="/api/v1")
