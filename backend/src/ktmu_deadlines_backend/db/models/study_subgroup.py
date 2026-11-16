from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .study_group import StudyGroup


class StudySubgroup(Base):
    __table_args__ = (UniqueConstraint("study_group_id", "name"),)

    name: Mapped[str]

    study_group_id: Mapped[int] = mapped_column(
        ForeignKey(StudyGroup.id, ondelete="CASCADE"), nullable=False
    )
    study_group: Mapped[StudyGroup] = relationship(
        lazy="selectin",
    )

    def __str__(self) -> str:
        return f"{self.study_group} ({self.name})"
