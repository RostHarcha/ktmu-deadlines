import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from ktmu_deadlines_backend.admin import setup_admin
from ktmu_deadlines_backend.api import api
from ktmu_deadlines_backend.db.core import engine

logging.basicConfig(level=logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    yield
    await engine.dispose()


app = FastAPI(
    title="КТМУ Дедлайны",
    lifespan=lifespan,
)
admin = setup_admin(app)
app.include_router(api)
