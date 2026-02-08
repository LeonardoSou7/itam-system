
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate

async def get_employees(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Employee]:
    result = await db.execute(select(Employee).offset(skip).limit(limit))
    return result.scalars().all()

async def create_employee(db: AsyncSession, employee: EmployeeCreate) -> Employee:
    db_employee = Employee(**employee.model_dump())
    db.add(db_employee)
    await db.commit()
    await db.refresh(db_employee)
    return db_employee
