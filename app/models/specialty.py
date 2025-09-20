from __future__ import annotations
from typing import Optional, List, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.user import User  # импорт только для type hints


class Speciality(SQLModel, table=True):
    __tablename__ = "specialities"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, unique=True)
    description: Optional[str] = Field(default=None)

    # 👇 здесь строка вместо прямого типа
    users: List["User"] = Relationship(back_populates="speciality")
