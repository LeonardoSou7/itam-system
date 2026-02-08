
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.api import deps
from app.schemas.employee import Employee, EmployeeCreate
from app.crud import employee as crud_employee
from app.models.user import User

router = APIRouter()

@router.get("/", response_model=List[Employee])
async def read_employees(
    db: AsyncSession = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(deps.get_current_active_user)
):
    employees = await crud_employee.get_employees(db, skip=skip, limit=limit)
    return employees

@router.post("/", response_model=Employee)
async def create_employee(
    employee: EmployeeCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(deps.get_current_active_user)
):
    return await crud_employee.create_employee(db=db, employee=employee)
