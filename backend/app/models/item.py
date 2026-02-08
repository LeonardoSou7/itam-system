
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Date, Enum, Text
from datetime import date, datetime
from typing import Optional
from enum import Enum as PyEnum
from app.db.base_class import Base

class ItemStatus(PyEnum):
    AVAILABLE = "AVAILABLE"
    IN_USE = "IN_USE"
    MAINTENANCE = "MAINTENANCE"
    DISCARDED = "DISCARDED"

class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    patrimony_number: Mapped[str] = mapped_column(String, unique=True, index=True)
    serial_number: Mapped[Optional[str]] = mapped_column(String, index=True, nullable=True)
    acquisition_date: Mapped[date] = mapped_column(Date)
    status: Mapped[ItemStatus] = mapped_column(Enum(ItemStatus), default=ItemStatus.AVAILABLE)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships are optional for now, but good to have for ORM
    # category = relationship("Category", back_populates="items")
