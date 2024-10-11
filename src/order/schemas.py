from datetime import datetime, time

from pydantic import BaseModel

class OrderReadSchema(BaseModel):
    id: int
    price: float # стоимость поездки
    date_trip: datetime # дата поездки
    travel_time: time # продолжительность поездки
    client_id: int
    driver_id: int
    created_at: datetime
    updated_at: datetime


class OrderCreateSchema(BaseModel):
    price: float # стоимость поездки
    date_trip: datetime # дата поездки
    travel_time: time # продолжительность поездки
    client_id: int
    driver_id: int

class OrderUpdateSchema(BaseModel):
    price: float # стоимость поездки
    date_trip: datetime # дата поездки
    travel_time: time # продолжительность поездки
    client_id: int
    driver_id: int


