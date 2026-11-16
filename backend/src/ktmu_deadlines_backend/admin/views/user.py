from ktmu_deadlines_backend.db.models import User

from .base import BaseModelView


class UserAdmin(BaseModelView, model=User):
    column_list = (User.id,)
