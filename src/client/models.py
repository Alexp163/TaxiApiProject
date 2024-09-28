from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base


class Client(Base):  # клиент
    __tablename__ = "client"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    rating: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now()
    )  # дата создания
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )  # дата обновления

    def __repr__(self):
        return f"{self.id} {self.name} {self.rating}"


