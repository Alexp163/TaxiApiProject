from datetime import datetime, timedelta  # timedelta - промежуток времени

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from database import Base


class Order(Base):
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[float] = mapped_column()  # стоимость поездки
    date_trip: Mapped[datetime] = mapped_column()  # дата поездки
    travel_time: Mapped[timedelta] = mapped_column()  # продолжительность поездки
    client: Mapped["Client"] = relationship("Client")
    client_id: Mapped[int | None] = mapped_column(ForeignKey("client.id"))
    driver: Mapped["Driver"] = relationship("Driver")
    driver_id: Mapped[int | None] = mapped_column(ForeignKey("driver.id"))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"{self.price} {self.date_trip} {self.travel_time} {self.driver_id} {self.client_id}"




