from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy.sql import func

from database import Base


class Driver(Base):  # модель водителя
    __tablename__ = "driver"

    id: Mapped[int] = mapped_column(primary_key=True)
    cars: Mapped[list["Car"]] = relationship("Car", secondary="driver2car")
    name: Mapped[str] = mapped_column()  # ФИО
    experience: Mapped[str] = mapped_column()  # опыт работы
    category: Mapped[str] = mapped_column()  # категория вод.прав
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"{self.name} {self.experience} {self.category}"

class Driver2Car(Base):
    __tablename__ = "driver2car"
    id: Mapped[int] = mapped_column(primary_key=True)
    driver_id: Mapped[int] = mapped_column(ForeignKey("driver.id"))
    car_id: Mapped[int] = mapped_column(ForeignKey("car.id"))

    def __repr__(self):
        return f"{self.driver_id} {self.car_id}"
