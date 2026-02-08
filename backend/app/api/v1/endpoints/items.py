
from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.api import deps
from app.schemas.item import Item, ItemCreate, Category, CategoryCreate
from app.crud import item as crud_item
from app.models.user import User

router = APIRouter()

@router.get("/", response_model=List[Item])
async def read_items(
    db: AsyncSession = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(deps.get_current_active_user)
):
    items = await crud_item.get_items(db, skip=skip, limit=limit)
    return items

@router.post("/", response_model=Item)
async def create_item(
    item: ItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(deps.get_current_active_user)
):
    return await crud_item.create_item(db=db, item=item)

@router.get("/categories", response_model=List[Category])
async def read_categories(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(deps.get_current_active_user)
):
    return await crud_item.get_categories(db)

@router.post("/categories", response_model=Category)
async def create_category(
    category: CategoryCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(deps.get_current_active_user)
):
    return await crud_item.create_category(db=db, category=category)
