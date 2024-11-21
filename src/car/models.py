from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from database import Base


class Car(Base):  # машина
    __tablename__ = "car"
    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str] = mapped_column()  # марка автомобиля
    category = relationship("Category")
    category_id: Mapped[int | None] = mapped_column(ForeignKey("category.id"))
    release: Mapped[str] = mapped_column()  # год выпуска
    configuration: Mapped[str] = mapped_column()  # комплектация автомобиля
    condition: Mapped[str] = mapped_column()  # техническое состояние автомобиля
    rent: Mapped[float] = mapped_column(server_default="0")  # счет аренды автомобиля
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())  # дата создания
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())  # дата обновления

    def __repr__(self):
        return (f"{self.id} {self.brand} {self.category_id} {self.release} {self.configuration} {self.condition}"
                f" {self.rent}")
