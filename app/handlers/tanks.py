import uuid

from fastapi import APIRouter, Depends, status, UploadFile
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.tank import TankCreate, TankResponse, TankUpdate
from app.services.tank_service import TankService

from pathlib import Path

router = APIRouter(
    prefix="/tanks",
    tags=["tanks"],
)

def get_tank_service(db: Session = Depends(get_db)) -> TankService:
    return TankService(db)

@router.post("/", response_model=TankResponse, status_code=status.HTTP_201_CREATED)
def create_tank(schema: TankCreate, service: TankService = Depends(get_tank_service)):
    return service.create_tank(schema)

@router.get("/", response_model=list[TankResponse])
def get_tanks(service: TankService = Depends(get_tank_service)):
    return service.get_tanks()

@router.get("/{tank_id}", response_model=TankResponse)
def get_tank(tank_id: int, service: TankService = Depends(get_tank_service)):
    return service.get_tank(tank_id)

@router.patch("/{tank_id}", response_model=TankResponse)
def update_tank(tank_id: int, schema: TankUpdate, service: TankService = Depends(get_tank_service)):
    return service.update_tank(tank_id, schema)

@router.delete("/{tank_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tank(tank_id: int, service: TankService = Depends(get_tank_service)) -> None:
    service.delete_tank(tank_id)

@router.post("/{tank_id}/photo", status_code=status.HTTP_201_CREATED)
async def load_photo(tank_id: int, file: UploadFile, service: TankService = Depends(get_tank_service)):
    MEDIA_DIR = Path(__file__).resolve().parent.parent / "media"
    MEDIA_DIR.mkdir(parents=True, exist_ok=True)

    suffix = Path(file.filename or "").suffix
    filename = f"{uuid.uuid4()}{suffix}"
    filepath = MEDIA_DIR / filename

    with open(filepath, "wb") as f:
        f.write(await file.read())

    return service.load_file(tank_id, f"/media/{filename}")
