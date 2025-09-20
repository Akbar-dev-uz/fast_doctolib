from typing import Generator

from sqlmodel import SQLModel, create_engine, Field, Session
from app.core.config import get_settings

settings = get_settings()
engine = create_engine(
    settings.database_url,
    echo=True,
    pool_pre_ping=True,
    future=True,
)


def get_session() -> Generator:
    with Session(engine) as session:
        yield session
