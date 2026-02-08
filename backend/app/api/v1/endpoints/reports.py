
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from backend.app.db.session import get_db
from backend.app.api import deps
from backend.app.models.item import Item, ItemStatus
from backend.app.models.user import User

router = APIRouter()

@router.get("/dashboard")
async def get_dashboard_stats(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(deps.get_current_active_user)
):
    total_items = await db.scalar(select(func.count(Item.id)))
    items_in_use = await db.scalar(select(func.count(Item.id)).where(Item.status == ItemStatus.IN_USE))
    items_available = await db.scalar(select(func.count(Item.id)).where(Item.status == ItemStatus.AVAILABLE))
    items_maintenance = await db.scalar(select(func.count(Item.id)).where(Item.status == ItemStatus.MAINTENANCE))
    
    return {
        "total_items": total_items,
        "items_in_use": items_in_use,
        "items_available": items_available,
        "items_maintenance": items_maintenance
    }
