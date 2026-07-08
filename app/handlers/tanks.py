from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.tanks import TankCreate, TankResponse, TankUpdate
from app.services.tank_service import TankService

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
