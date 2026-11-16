import enum
from datetime import datetime
from typing import Annotated

from sqlalchemy import DateTime, Enum, MetaData, func
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column

type IntPk = Annotated[
    int,
    mapped_column(primary_key=True),
]

type StrPk = Annotated[
    str,
    mapped_column(primary_key=True),
]

type AutoNowCreate = Annotated[
    datetime,
    mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    ),
]

type AutoNow = Annotated[
    datetime,
    mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    ),
]


def pg_enum(enum: type[enum.Enum], name: str) -> Enum:
    def values_callable(e: type[enum.Enum]):
        return [member.value for member in e]

    return Enum(
        enum,
        values_callable=values_callable,
        name=name,
    )


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_N_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        },
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    def __str__(self) -> str:
        return f"{self.__class__.__name__} #{self.id}"

    id: Mapped[IntPk]

    created_at: Mapped[AutoNowCreate]

    updated_at: Mapped[AutoNow]
