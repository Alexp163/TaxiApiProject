from pydantic import BaseModel

from datetime import datetime


class CarReadSchema(BaseModel):
    id: int
    brand: str # марка автомобиля
    release: str # год выпуска
    configuration: str # комплектация автомобиля
    condition: str # состояние автомобиля
    created_at: datetime  # дата создания
    updated_at: datetime  # дата обновления


class CarCreateSchema(BaseModel):
    brand: str
    release: str
    configuration: str
    condition: str


class CarUpdateSchema(BaseModel):
    brand: str
    release: str
    configuration: str
    condition: str


