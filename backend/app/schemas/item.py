
from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from backend.app.models.item import ItemStatus

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    class Config:
        from_attributes = True

class ItemBase(BaseModel):
    category_id: int
    patrimony_number: str
    serial_number: Optional[str] = None
    acquisition_date: date
    status: ItemStatus = ItemStatus.AVAILABLE
    notes: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    category_id: Optional[int] = None
    patrimony_number: Optional[str] = None
    serial_number: Optional[str] = None
    acquisition_date: Optional[date] = None
    status: Optional[ItemStatus] = None
    notes: Optional[str] = None

class Item(ItemBase):
    id: int
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True
