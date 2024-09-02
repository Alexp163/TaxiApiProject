from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base


class Driver(Base):  # модель водителя
    __tablename__ = "driver"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()  # ФИО
    experience: Mapped[str] = mapped_column()  # опыт работы
    category: Mapped[str] = mapped_column()  # категория вод.прав
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

