from datetime import datetime

from pydantic import BaseModel


class DriverReadSchema(BaseModel):
    id: int
    name: str
    experience: str
    category: str
    created_at: datetime
    updated_at: datetime


class DriverCreateSchema(BaseModel):
    name: str
    experience: str
    category: str


class DriverUpdateSchema(BaseModel):
    name: str
    experience: str
    category: str
