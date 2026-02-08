
import asyncio
import logging

from backend.app.db.session import AsyncSessionLocal
from backend.app.crud.user import create_user, get_user_by_username
from backend.app.schemas.user import UserCreate
from backend.app.models.user import UserRole
from backend.app.db.base import Base

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def init_db():
    async with AsyncSessionLocal() as session:
        user = await get_user_by_username(session, "admin")
        if not user:
            logger.info("Creating admin user")
            user_in = UserCreate(
                username="admin",
                password="leo1234567",
                role=UserRole.ADMIN,
                active=True
            )
            await create_user(session, user_in)
            logger.info("Admin user created")
        else:
            logger.info("Admin user already exists")

def main():
    asyncio.run(init_db())

if __name__ == "__main__":
    main()
