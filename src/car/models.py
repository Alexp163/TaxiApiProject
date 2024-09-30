from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base


class Car(Base):  # машина
    __tablename__ = "car"
    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str] = mapped_column()  # марка автомобиля
    release: Mapped[str] = mapped_column()  # год выпуска
    configuration: Mapped[str] = mapped_column()  # комплектация автомобиля
    condition: Mapped[str] = mapped_column()  # состояние автомобиля
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())  # дата создания
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())  # дата обновления

    def __repr__(self):
        return f"{self.id} {self.brand} {self.release} {self.configuration} {self.condition}"

