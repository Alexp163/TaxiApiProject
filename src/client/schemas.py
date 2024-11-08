from datetime import datetime
from pydantic import BaseModel


class ClientReadSchema(BaseModel):
    id: int
    name: str
    rating: float
    wallet: float
    created_at: datetime
    updated_at: datetime


class ClientCreateSchema(BaseModel):
    name: str
    rating: float
    wallet: float


class ClientUpdateSchema(BaseModel):
    name: str
    rating: float
    wallet: float
