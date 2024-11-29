from datetime import datetime

from fastapi import APIRouter, status, Depends
from sqlalchemy import insert, select, delete, update

from database import get_async_session
from .models import Car
from .schemas import CarCreateSchema, CarReadSchema, CarUpdateSchema

router = APIRouter(tags=["cars"], prefix="/cars")

# fmt: off
@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) создание машины
async def create_car(car: CarCreateSchema, session=Depends(get_async_session)) -> CarReadSchema:
    statement = insert(Car).values(
        brand=car.brand,
        release=car.release,
        configuration=car.configuration,
        condition=car.condition
    ).returning(Car)
    result = await session.scalar(statement)
    await session.commit()
    return result
# fmt: on

# fmt: off
@router.get("/", status_code=status.HTTP_202_ACCEPTED)  # 2) получение данных о всех машинах
async def get_cars(start_date: datetime | None = None,
                   end_date: datetime | None = None, session=Depends(get_async_session)) -> list[CarReadSchema]:
    statement = select(Car).where(Car.created_at >= start_date).where(Car.created_at <= end_date)
    result = await session.scalar(statement)
    return list(result)
# fmt: on

@router.get("/{car_id}", status_code=status.HTTP_202_ACCEPTED)  # 3) Получение данных о машине по id
async def get_car_by_id(car_id: int, session=Depends(get_async_session)) -> CarReadSchema:
    statement = select(Car).where(Car.id == car_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{car_id}", status_code=status.HTTP_204_NO_CONTENT)  #  4) Удаление машины по id
async def delete_car_by_id(car_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Car).where(Car.id == car_id)
    await session.execute(statement)
    await session.commit()

# fmt: off
@router.put("/{car_id}", status_code=status.HTTP_200_OK)  # 5) Обновление данных
async def update_car_by_id(car_id: int, car: CarUpdateSchema, session=Depends(get_async_session)) -> CarReadSchema:
    statement = update(Car).where(Car.id == car_id).values(
        brand=car.brand,
        release=car.release,
        configuration=car.configuration,
        condition=car.condition
    ).returning(Car)
    result = await session.scalar(statement)
    await session.commit()
    return result
# fmt: on
