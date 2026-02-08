
# Import all the models, so that Base has them before being
# imported by Alembic
from backend.app.db.base_class import Base  # noqa
from backend.app.models.user import User  # noqa
from backend.app.models.employee import Employee  # noqa
from backend.app.models.category import Category  # noqa
from backend.app.models.item import Item  # noqa
from backend.app.models.movement import Movement  # noqa
