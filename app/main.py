import sys
from pathlib import Path

from fastapi import FastAPI

from app.handlers.health import router as health_router
from app.handlers.auth import router as auth_router
from app.handlers.tanks import router as tank_router
from app.handlers.users import router as users_router
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

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(health_router)
app.include_router(tank_router)
app.include_router(users_router)

@app.get("/")
def root():
    return {
        "message": f"{settings.app_name} is running",
    }


