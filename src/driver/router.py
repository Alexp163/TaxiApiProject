from fastapi import APIRouter, Depends, status
from sqlalchemy import select, insert, delete, update

from database import get_async_session
from .dependecies import Order, OrderReadSchema
from .models import Driver
from .schemas import DriverCreateSchema, DriverReadSchema, DriverUpdateSchema

router = APIRouter(tags=["drivers"], prefix="/drivers")


@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) Создание модели водителя
async def create_driver(driver: DriverCreateSchema, session=Depends(get_async_session)) -> DriverReadSchema:
    statement = insert(Driver).values(
        name=driver.name,
        experience=driver.experience,
        category=driver.category
    ).returning(Driver)
    result = await session.scalar(statement)
    await session.commit()
    return result


@router.get("/", status_code=status.HTTP_202_ACCEPTED)  # 2) Получение данных о всех водителях
async def get_drivers(session=Depends(get_async_session)) -> list[DriverReadSchema]:  # "Depends" - зависит
    statement = select(Driver)
    result = await session.scalars(statement)
    return result


@router.get("/{driver_id}", status_code=status.HTTP_202_ACCEPTED)  # 3) Получение данных о водителе по id
async def get_driver_by_id(driver_id: int, session=Depends(get_async_session)) -> DriverReadSchema:
    statement = select(Driver).where(Driver.id == driver_id)
    result = await session.scalar(statement)
    return result


@router.get("/{driver_id}/orders", status_code=status.HTTP_200_OK)  # выводит список заказов водителя
async def get_driver_orders(driver_id: int, session=Depends(get_async_session)) -> list[OrderReadSchema]:
    statement = select(Order).where(Order.driver_id == driver_id)
    result = await session.scalars(statement)
    return result


@router.delete("/{driver_id}", status_code=status.HTTP_204_NO_CONTENT)  # 4) Удаление водителя по id
async def delete_driver_by_id(driver_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Driver).where(Driver.id == driver_id)
    await session.execute(statement)
    await session.commit()


@router.put("/{driver_id}", status_code=status.HTTP_200_OK)
async def update_driver_by_id(driver_id: int, driver: DriverUpdateSchema,
                              session=Depends(get_async_session)) -> DriverUpdateSchema:
    statement = update(Driver).where(Driver.id == driver_id).values(
        name=driver.name,
        experience=driver.experience,
        category=driver.category
    ).returning(Driver)
    result = await session.scalar(statement)
    await session.commit()
    return result
