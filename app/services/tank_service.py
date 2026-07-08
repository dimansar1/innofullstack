from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.tank import Tank
from app.repositories.tank_repository import TankRepository
from app.schemas.tanks import TankCreate, TankUpdate


class TankService:

    def __init__(self, db: Session):
        self.repository = TankRepository(db)

    def create_tank(self, schema: TankCreate) -> Tank:
        tank = Tank(
            title=schema.title,
            photo_path=schema.photo_path,
            health=schema.health,
            damage=schema.damage,
            armor=schema.armor,
            history=schema.history,
            recommendation=schema.recommendation,
            category=schema.category,
            nation=schema.nation,
            level=schema.level,
        )

        return self.repository.create(tank)
    
    def get_tanks(self) -> list[Tank]:
        return self.repository.get_all()
    
    def get_tank(self, tank_id: int) -> Tank:
        tank = self.repository.get_by_id(tank_id)

        if tank is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tank not found",
            )

        return tank
    
    def update_tank(self, tank_id: int, schema: TankUpdate) -> Tank:
        tank = self.get_tank(tank_id)

        if schema.title is None and schema.category is None and schema.nation is None and schema.level is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="At least one field must be provided",
            )

        if schema.title is not None:
            tank.title = schema.title

        if schema.category is not None:
            tank.category = schema.category

        if schema.nation is not None:
            tank.nation = schema.nation

        if schema.level is not None:
            tank.level = schema.level

        tank.photo_path = schema.photo_path
        tank.health = schema.health
        tank.damage = schema.damage
        tank.armor = schema.armor
        tank.history = schema.history
        tank.recommendation = schema.recommendation

        return self.repository.update(tank)
    
    def delete_tank(self, tank_id: int) -> None:
        self.repository.delete(tank_id)