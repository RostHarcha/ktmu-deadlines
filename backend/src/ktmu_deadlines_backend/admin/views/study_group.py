from ktmu_deadlines_backend.db.models import StudyGroup

from .base import BaseModelView


class StudyGroupAdmin(BaseModelView, model=StudyGroup):
    column_list = (
        StudyGroup.id,
        StudyGroup.name,
    )
