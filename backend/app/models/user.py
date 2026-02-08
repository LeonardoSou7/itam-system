
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, Enum
import uuid
from backend.app.db.base_class import Base
from enum import Enum as PyEnum

class UserRole(PyEnum):
    ADMIN = "ADMIN"
    COMMON = "COMMON"

class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.COMMON)
    active: Mapped[bool] = mapped_column(Boolean, default=True)
