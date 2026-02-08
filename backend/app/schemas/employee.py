
from pydantic import BaseModel
from typing import Optional

class EmployeeBase(BaseModel):
    name: str
    department: str
    email: Optional[str] = None
    active: bool = True

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int
    class Config:
        from_attributes = True
