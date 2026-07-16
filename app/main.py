import sys
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from pathlib import Path

from app.handlers.health import router as health_router
from app.handlers.auth import router as auth_router
from app.handlers.tanks import router as tank_router
from app.handlers.users import router as users_router
from app.handlers.favourites import router as favourites_router
from app.models.tank import Tank
from app.models.user import User
from app.config.config import get_settings
from app.database import Base, engine

settings = get_settings()

app = FastAPI(
    title = settings.app_name,
    version = settings.app_version,
    debug = settings.debug,
)

MEDIA_DIR = Path(__file__).resolve().parent / "media"
MEDIA_DIR.mkdir(parents=True, exist_ok=True)

app.mount(
    "/media",
    StaticFiles(directory=MEDIA_DIR),
    name="media",
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(health_router)
app.include_router(tank_router)
app.include_router(users_router)
app.include_router(favourites_router)

@app.get("/")
def root():
    return {
        "message": f"{settings.app_name} is running",
    }


