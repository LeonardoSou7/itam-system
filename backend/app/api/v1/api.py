
from fastapi import APIRouter
from app.api.v1.endpoints import auth, items, employees, movements, reports

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(employees.router, prefix="/employees", tags=["employees"])
api_router.include_router(movements.router, prefix="/movements", tags=["movements"])
api_router.include_router(reports.router, prefix="/reports", tags=["reports"])
