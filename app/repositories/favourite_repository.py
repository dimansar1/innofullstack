from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from app.models.favourite import Favourite

from app.repositories.tank_repository import TankRepository 

class FavouriteRepository:

    def __init__(self, db: Session):
        self.db = db
        self.tank_repository = TankRepository(db)

    def create(self, favourite: Favourite) -> Favourite:
        if not self.tank_repository.get_by_id(favourite.tank_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tank not found",
            )
        
        try:
            self.db.add(favourite)
            self.db.commit()
            self.db.refresh(favourite)

            return favourite
        except:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Tank already exists",
            )
            
    
    def get_all_by_user_id(self, user_id: int) -> list[Favourite]:
        return self.db.query(Favourite).filter(Favourite.user_id == user_id).all()
    
    def delete(self, tank_id: int, user_id: int) -> None:
        self.db.query(Favourite).filter(Favourite.tank_id == tank_id, Favourite.user_id == user_id).delete()
        self.db.commit()

    def delete_by_tank_id(self, tank_id: int) -> None:
        self.db.query(Favourite).filter(Favourite.tank_id == tank_id).delete()
        self.db.commit()


