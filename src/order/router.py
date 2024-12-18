from datetime import datetime

from fastapi import APIRouter, status, Depends
from sqlalchemy import insert, select, delete, update

from .dependencies import Client, Driver, Car
from database import get_async_session, Base, AsyncSession
from .models import Order
from .schemas import OrderCreateSchema, OrderReadSchema, OrderUpdateSchema
from .utils import increase_wallet


router = APIRouter(tags=["orders"], prefix="/orders")



# fmt: off
@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) Создание заказа
async def create_order(order: OrderCreateSchema, session=Depends(get_async_session)) -> OrderReadSchema:
    statement = insert(Order).values(
            price=order.price,
            date_trip=order.date_trip,
            travel_time=order.travel_time,
            client_id=order.client_id,
            driver_id=order.driver_id,
            car_id=order.car_id
    ).returning(Order)
    result = await session.scalar(statement)
    await increase_wallet(Client, order.price, session, -1, order.client_id)
    await increase_wallet(Driver, order.price, session, 0.75, order.driver_id)
    await increase_wallet(Car, order.price, session, 0.25, order.car_id)
    await session.commit()
    return result
# fmt: on


# fmt: off
@router.get("/", status_code=status.HTTP_200_OK)  # 2) получение данных о всех заказах
async def get_orders(start_date: datetime | None = None,
                     end_date: datetime | None = None,
                     start_price: float | None = None,
                     end_price: float | None = None,
    session=Depends(get_async_session)) -> list[OrderReadSchema]:
    statement = select(Order)
    if start_date is not None:
        statement = statement.where(Order.created_at >= start_date)
    if end_date is not None:
        statement = statement.where(Order.created_at <= end_date)
    if start_price is not None:
        statement = statement.where(Order.price >= start_price)
    if end_price is not None:
        statement = statement.where(Order.price <= end_price)
    result = await session.scalars(statement)
    return list(result)
# fmt: on


@router.get("/{order_id}", status_code=status.HTTP_200_OK)  # 3) получение данных о заказе по id
async def get_order_by_id(order_id: int, session=Depends(get_async_session)) -> OrderReadSchema:
    statement = select(Order).where(Order.id == order_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)  # 4) удаление заказа по id
async def delete_order_by_id(order_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Order).where(Order.id == order_id)
    await session.execute(statement)
    await session.commit()


# fmt: off
@router.put("/{order_id}", status_code=status.HTTP_200_OK)  # 5) обновление заказа по id
async def update_order_by_id(order_id: int, order: OrderUpdateSchema,
                             session=Depends(get_async_session)) -> OrderReadSchema:
    statement = update(Order).where(Order.id == order_id).values(
            price=order.price,  # стоимость поездки
            date_trip=order.date_trip,  # дата поездки
            travel_time=order.travel_time,  # продолжительность поездки
            client_id=order.client_id,
            driver_id=order.driver_id,
            car_id=order.car_id
        ).returning(Order)
    result = await session.scalar(statement)
    await session.commit()
    return result
# fmt: on
