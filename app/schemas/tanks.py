from pydantic import BaseModel

class TankCreateRequest(BaseModel):
    title: str
    photo_path: str
    health: str
    damage: str
    armor: str
    history: str
    recommendation: str
    category: str
    nation: str
    level: str

class TankCreateResponse(BaseModel):
    id: int
    title: str
    photo_path: str
    health: str
    damage: str
    armor: str
    history: str
    recommendation: str
    category: str
    nation: str
    level: str
