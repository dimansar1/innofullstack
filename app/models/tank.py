from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.favourite import favourite


class Tank(Base):
    __tablename__ = "tanks"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    photo_path: Mapped[str] = mapped_column(String, default='-')
    health: Mapped[str] = mapped_column(String, default='-')
    damage: Mapped[str] = mapped_column(String, default='-')
    armor: Mapped[str] = mapped_column(String, default='-')
    history: Mapped[str] = mapped_column(String, default='Историческая справка о данном танке отсутствует')
    recommendation: Mapped[str] = mapped_column(String, default='Рекомендации по игре на данном танке отсутстуют')
    category: Mapped[str] = mapped_column(String, nullable=False)
    nation: Mapped[str] = mapped_column(String, nullable=False)
    level: Mapped[str] = mapped_column(String, nullable=False)
    users = relationship("User", secondary=favourite, back_populates="tanks")
