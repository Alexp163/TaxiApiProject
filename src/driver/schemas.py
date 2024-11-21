from datetime import datetime

from pydantic import BaseModel


class DriverReadSchema(BaseModel):
    id: int
    name: str
    experience: str
    category: str
    wallet: float
    created_at: datetime
    updated_at: datetime


class DriverCreateSchema(BaseModel):
    name: str
    experience: str
    category: str
    wallet: float


class DriverUpdateSchema(BaseModel):
    name: str
    experience: str
    category: str
    wallet: float

