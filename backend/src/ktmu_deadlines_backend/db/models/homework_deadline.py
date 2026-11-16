from datetime import date

from sqlalchemy import CheckConstraint, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .homework import Homework
from .study_group import StudyGroup
from .study_subgroup import StudySubgroup


class HomeworkDeadline(Base):
    __table_args__ = (
        CheckConstraint(
            "num_nonnulls(study_group_id, study_subgroup_id) = 1",
            name="exactly_one_audience",
        ),
    )

    homework_id: Mapped[int] = mapped_column(
        ForeignKey(Homework.id, ondelete="CASCADE"),
        nullable=False,
    )
    homework: Mapped[Homework] = relationship()

    study_group_id: Mapped[int | None] = mapped_column(
        ForeignKey(StudyGroup.id, ondelete="CASCADE"),
    )
    study_group: Mapped[StudyGroup | None] = relationship()

    study_subgroup_id: Mapped[int | None] = mapped_column(
        ForeignKey(StudySubgroup.id, ondelete="CASCADE"),
    )
    study_subgroup: Mapped[StudySubgroup | None] = relationship()

    deadline_at: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )
