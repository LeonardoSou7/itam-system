
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.app.models.item import Item, ItemStatus
from backend.app.models.category import Category
from backend.app.schemas.item import ItemCreate, ItemUpdate, CategoryCreate

async def get_items(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Item]:
    result = await db.execute(select(Item).offset(skip).limit(limit))
    return result.scalars().all()

async def create_item(db: AsyncSession, item: ItemCreate) -> Item:
    db_item = Item(**item.model_dump())
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item

async def get_categories(db: AsyncSession) -> List[Category]:
    result = await db.execute(select(Category))
    return result.scalars().all()

async def create_category(db: AsyncSession, category: CategoryCreate) -> Category:
    db_category = Category(**category.model_dump())
    db.add(db_category)
    await db.commit()
    await db.refresh(db_category)
    return db_category
