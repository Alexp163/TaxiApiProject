from datetime import datetime

from fastapi import APIRouter, status, Depends
from sqlalchemy import insert, select, delete, update

from database import get_async_session
from .models import Order
from .schemas import OrderCreateSchema, OrderReadSchema, OrderUpdateSchema

router = APIRouter(tags=["orders"], prefix="/orders")

@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) Создание заказа
async def create_order(order: OrderCreateSchema, start_date: datetime | None = None, end_date: datetime | None = None, session=Depends(get_async_session)) -> OrderReadSchema:
    statement = insert(Order).values(
        price=order.price,
        date_trip=order.date_trip,
        travel_time=order.travel_time,
        client_id=order.client_id,
        driver_id=order.driver_id
    ).returning(Order)
    result = await session.scalar(statement)
    await session.commit()
    return  result


@router.get("/", status_code=status.HTTP_200_OK)  # 2) получение данных о всех заказах
async def get_orders(start_date: datetime | None = None, end_date: datetime | None = None, session=Depends(get_async_session)) -> list[OrderReadSchema]:
    statement = select(Order).where(Order.created_at >= start_date).where(Order.created_at <= end_date)
    result = await session.scalars(statement)
    return list(result)



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


@router.put("/{order_id}", status_code=status.HTTP_200_OK)  # 5) обновление заказа по id
async def update_order_by_id(order_id: int, order: OrderUpdateSchema,
                             session=Depends(get_async_session)) -> OrderReadSchema:
    statement = update(Order).where(Order.id == order_id).values(
    price=order.price, # стоимость поездки
    date_trip=order.date_trip, # дата поездки
    travel_time=order.travel_time, # продолжительность поездки
    client_id=order.client_id,
    driver_id=order.driver_id
    ).returning(Order)
    result = await session.scalar(statement)
    await session.commit()
    return result

