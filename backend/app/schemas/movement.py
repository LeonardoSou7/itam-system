
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.movement import MovementType

class MovementBase(BaseModel):
    item_id: int
    employee_id: Optional[int] = None
    type: MovementType
    observation: Optional[str] = None
    movement_date: datetime = datetime.utcnow()

class MovementCreate(MovementBase):
    pass

class Movement(MovementBase):
    id: int
    user_id: str
    class Config:
        from_attributes = True

# Specific schemas for actions
class LoanCreate(BaseModel):
    item_id: int
    employee_id: int
    observation: Optional[str] = None

class ReturnCreate(BaseModel):
    item_id: int
    observation: Optional[str] = None
    is_defective: bool = False # Logic to change status to MAINTENANCE
