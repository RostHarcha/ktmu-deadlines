from ktmu_deadlines_backend.db.models import HomeworkDeadline

from .base import BaseModelView


class HomeworkDeadlineAdmin(BaseModelView, model=HomeworkDeadline):
    column_list = (
        HomeworkDeadline.homework,
        HomeworkDeadline.study_group,
        HomeworkDeadline.study_subgroup,
        HomeworkDeadline.deadline_at,
    )
