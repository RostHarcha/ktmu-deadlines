from functools import cache
from pathlib import Path

from alembic.config import Config
from alembic.script import ScriptDirectory
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from ktmu_deadlines_backend.db.deps import DBSessionDep

api = APIRouter(prefix="/api")


@api.get("/health", tags=["Healthcheck"])
async def health() -> dict[str, str]:
    return {"status": "ok"}


@cache
def _head_revision() -> str | None:
    config = Config(Path(__file__).resolve().parents[3] / "alembic.ini")
    return ScriptDirectory.from_config(config).get_current_head()


@api.get("/ready", tags=["Healthcheck"])
async def ready(db: DBSessionDep):
    try:
        revision = await db.scalar(
            text("SELECT version_num FROM alembic_version")
        )
        if revision is not None and revision == _head_revision():
            return {"status": "ready"}
    except SQLAlchemyError:
        return JSONResponse({"status": "not_ready"}, status_code=503)
    return JSONResponse({"status": "not_ready"}, status_code=503)
