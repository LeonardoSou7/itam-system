
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey, DateTime, Enum
from datetime import datetime
from typing import Optional
from enum import Enum as PyEnum
from app.db.base_class import Base

class MovementType(PyEnum):
    LOAN = "LOAN"
    RETURN = "RETURN"
    MAINTENANCE_SEND = "MAINTENANCE_SEND"
    MAINTENANCE_RETURN = "MAINTENANCE_RETURN"
    DISCARD = "DISCARD"

class Movement(Base):
    __tablename__ = "movements"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"))
    employee_id: Mapped[Optional[int]] = mapped_column(ForeignKey("employees.id"), nullable=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id")) # Admin/User who registered the movement
    type: Mapped[MovementType] = mapped_column(Enum(MovementType))
    movement_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    observation: Mapped[Optional[str]] = mapped_column(String, nullable=True)
