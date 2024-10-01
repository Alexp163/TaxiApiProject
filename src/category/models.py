from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base


class Category(Base):  # категория машины
    __tablename__ = "category"
    id: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()  # название категории
    schedule: Mapped[str] = mapped_column()  # часы работы в категории
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())  # дата создания
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())  # дата обновления

    def __repr__(self):
        return f"{self.id} {self.title} {self.schedule}"

