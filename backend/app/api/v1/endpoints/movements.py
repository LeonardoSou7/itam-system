
from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.db.session import get_db
from backend.app.api import deps
from backend.app.schemas.movement import Movement, LoanCreate, ReturnCreate
from backend.app.crud import movement as crud_movement
from backend.app.models.user import User

router = APIRouter()

@router.post("/loan", response_model=Movement)
async def create_loan(
    loan: LoanCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(deps.get_current_active_user)
):
    return await crud_movement.create_loan(db, loan, user_id=current_user.id)

@router.post("/return", response_model=Movement)
async def create_return(
    return_data: ReturnCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(deps.get_current_active_user)
):
    return await crud_movement.create_return(db, return_data, user_id=current_user.id)

@router.get("/item/{item_id}", response_model=List[Movement])
async def get_item_history(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(deps.get_current_active_user)
):
    return await crud_movement.get_movements_by_item(db, item_id)
