from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.favourite import Favourite
from app.repositories.favourite_repository import FavouriteRepository

class FavouriteService:

    def __init__(self, db: Session):
        self.repository = FavouriteRepository(db)

    def create_favourite(self, tank_id: int, user_id: int) -> Favourite:
        favourite = Favourite(
            tank_id=tank_id,
            user_id=user_id,  
        )

        return self.repository.create(favourite)
    
    def get_favourites_by_user_id(self, user_id: int) -> list[Favourite]:
        return self.repository.get_all_by_user_id(user_id)
    
    def delete_favourite(self, tank_id: int, user_id: int) -> None:
        self.repository.delete(tank_id, user_id)