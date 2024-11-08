from datetime import datetime

from pydantic import BaseModel


class CategoryReadSchema(BaseModel):
    id: int
    title: str
    schedule: str
    created_at: datetime
    updated_at: datetime


class CategoryCreateSchema(BaseModel):
    title: str
    schedule: str


class CategoryUpdateSchema(BaseModel):
    title: str
    schedule: str
