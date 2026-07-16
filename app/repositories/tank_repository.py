from sqlalchemy.orm import Session

from app.models.tank import Tank

from typing import Optional

class TankRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, tank: Tank) -> Tank:
        self.db.add(tank)
        self.db.commit()
        self.db.refresh(tank)

        return tank
    
    def update(self, tank: Tank) -> Tank:
        self.db.add(tank)
        self.db.commit()
        self.db.refresh(tank)

        return tank
    
    def get_all(self) -> list[Tank]:
        return self.db.query(Tank).all()
    
    def get_by_id(self, tank_id: int) -> Optional[Tank]:
        stmt = self.db.query(Tank).filter(Tank.id == tank_id)
        return (
            self.db.scalars(stmt).one_or_none()
        )
    
    def delete(self, tank_id: int) -> None:
        self.db.query(Tank).filter(Tank.id == tank_id).delete()
        self.db.commit()
    
    def load_file(self, tank_id: int, filename: str):
        tank = self.get_by_id(tank_id)
        tank.photo_path = filename
        self.db.commit()