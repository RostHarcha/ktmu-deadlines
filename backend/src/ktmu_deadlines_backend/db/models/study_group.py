from sqlalchemy.orm import Mapped

from .base import Base


class StudyGroup(Base):
    name: Mapped[str]

    def __str__(self) -> str:
        return self.name
