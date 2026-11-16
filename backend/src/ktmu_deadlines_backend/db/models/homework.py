from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .subject import Subject


class Homework(Base):
    subject_id: Mapped[int] = mapped_column(
        ForeignKey(Subject.id, ondelete="CASCADE"), nullable=False
    )
    subject: Mapped[Subject] = relationship(
        lazy="selectin",
    )

    description: Mapped[str] = mapped_column(Text)

    def __str__(self) -> str:
        return f"{self.subject} - {self.description[:20]}..."
