from ktmu_deadlines_backend.db.models import Subject

from .base import BaseModelView


class SubjectAdmin(BaseModelView, model=Subject):
    column_list = (
        Subject.id,
        Subject.name,
    )
