from fastapi import FastAPI
from sqladmin import Admin

from ktmu_deadlines_backend.db.core import engine

from .views.homework import HomeworkAdmin
from .views.homework_deadline import HomeworkDeadlineAdmin
from .views.study_group import StudyGroupAdmin
from .views.study_subgroup import StudySubgroupAdmin
from .views.subject import SubjectAdmin
from .views.user import UserAdmin


def setup_admin(app: FastAPI) -> Admin:
    admin = Admin(
        app=app,
        engine=engine,
    )
    for view in (
        HomeworkAdmin,
        HomeworkDeadlineAdmin,
        StudyGroupAdmin,
        StudySubgroupAdmin,
        SubjectAdmin,
        UserAdmin,
    ):
        admin.add_view(view)
    return admin
