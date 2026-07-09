from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class TankCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    photo_path: str = Field(default='-', min_length=1, max_length=200)
    health: str = Field(default='-', min_length=1, max_length=200)
    damage: str = Field(default='-', min_length=1, max_length=200)
    armor: str = Field(default='-', min_length=1, max_length=200)
    history: str = Field(default='Историческая справка о данном танке отсутствует', min_length=1, max_length=5000)
    recommendation: str = Field(default='Рекомендации по игре на данном танке отсутстуют', min_length=1, max_length=5000)
    category: str = Field(min_length=1, max_length=50)
    nation: str = Field(min_length=1, max_length=50)
    level: str = Field(min_length=1, max_length=10)

class TankUpdate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    photo_path: Optional[str] = Field(default='-', min_length=1, max_length=200)
    health: Optional[str] = Field(default='-', min_length=1, max_length=200)
    damage: Optional[str] = Field(default='-', min_length=1, max_length=200)
    armor: Optional[str] = Field(default='-', min_length=1, max_length=200)
    history: Optional[str] = Field(default='Историческая справка о данном танке отсутствует', min_length=1, max_length=5000)
    recommendation: Optional[str] = Field(default='Рекомендации по игре на данном танке отсутстуют', min_length=1, max_length=5000)
    category: str = Field(min_length=1, max_length=50)
    nation: str = Field(min_length=1, max_length=50)
    level: str = Field(min_length=1, max_length=10)

class TankResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

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


