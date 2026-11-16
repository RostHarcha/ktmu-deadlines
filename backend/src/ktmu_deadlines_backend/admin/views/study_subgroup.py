from ktmu_deadlines_backend.db.models import StudySubgroup

from .base import BaseModelView


class StudySubgroupAdmin(BaseModelView, model=StudySubgroup):
    column_list = (
        StudySubgroup.id,
        StudySubgroup.name,
        StudySubgroup.study_group,
    )
