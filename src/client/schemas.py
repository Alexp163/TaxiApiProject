from datetime import datetime
from pydantic import BaseModel


class ClientReadSchema(BaseModel):
    id: int
    name: str
    rating: str
    created_at: datetime
    updated_at: datetime


class ClientCreateSchema(BaseModel):
    name: str
    rating: str


class ClientUpdateSchema(BaseModel):
    name: str
    rating: str

