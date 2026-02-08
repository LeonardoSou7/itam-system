
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime
from fastapi import HTTPException, status
from backend.app.models.movement import Movement, MovementType
from backend.app.models.item import Item, ItemStatus
from backend.app.schemas.movement import LoanCreate, ReturnCreate

async def create_loan(db: AsyncSession, loan: LoanCreate, user_id: str) -> Movement:
    # 1. Check if item exists and is available
    result = await db.execute(select(Item).where(Item.id == loan.item_id))
    item = result.scalars().first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if item.status != ItemStatus.AVAILABLE:
        raise HTTPException(status_code=409, detail=f"Item is not available (Status: {item.status})")

    # 2. Create Movement record
    movement = Movement(
        item_id=loan.item_id,
        employee_id=loan.employee_id,
        user_id=user_id,
        type=MovementType.LOAN,
        movement_date=datetime.utcnow(),
        observation=loan.observation
    )
    db.add(movement)

    # 3. Update Item status
    item.status = ItemStatus.IN_USE
    db.add(item)

    await db.commit()
    await db.refresh(movement)
    return movement

async def create_return(db: AsyncSession, return_data: ReturnCreate, user_id: str) -> Movement:
    # 1. Get item
    result = await db.execute(select(Item).where(Item.id == return_data.item_id))
    item = result.scalars().first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # 2. Check if item is actually OUT (optional, but good practice)
    # logic: if it's already available, why return it? 
    # But maybe it was lost and found? Let's allow it but warn or just log.
    # Strict mode:
    if item.status == ItemStatus.AVAILABLE:
         raise HTTPException(status_code=400, detail="Item is already available")

    # 3. Create Movement
    movement = Movement(
        item_id=return_data.item_id,
        user_id=user_id,
        type=MovementType.RETURN,
        movement_date=datetime.utcnow(),
        observation=return_data.observation
    )
    db.add(movement)

    # 4. Update Item status
    if return_data.is_defective:
        item.status = ItemStatus.MAINTENANCE
    else:
        item.status = ItemStatus.AVAILABLE
    
    db.add(item)
    await db.commit()
    await db.refresh(movement)
    return movement

async def get_movements_by_item(db: AsyncSession, item_id: int) -> List[Movement]:
    result = await db.execute(select(Movement).where(Movement.item_id == item_id).order_by(Movement.movement_date.desc()))
    return result.scalars().all()
