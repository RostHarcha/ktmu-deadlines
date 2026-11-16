from ktmu_deadlines_backend.db.models import Homework

from .base import BaseModelView


class HomeworkAdmin(BaseModelView, model=Homework):
    column_list = (
        Homework.id,
        Homework.subject,
        Homework.description,
    )
