from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Optional, TYPE_CHECKING

from pydantic import EmailStr
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.specialty import Speciality


class Role(str, Enum):
    patient = "Patient"
    doctor = "Doctor"


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    email: EmailStr = Field(unique=True)
    password: str = Field(nullable=False)
    full_name: str = Field(nullable=False)
    phone: str = Field(nullable=False)
    role: Role = Field(nullable=False, default=Role.patient.value)
    bio: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.now)

    speciality_id: Optional[int] = Field(default=None, foreign_key="specialities.id")
    speciality: Optional["Speciality"] = Relationship(back_populates="users")
