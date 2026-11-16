from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .core import get_session

type DBSessionDep = Annotated[AsyncSession, Depends(get_session)]
