from fastapi import APIRouter, Depends, status
from sqlalchemy import insert, select, delete, update

from database import get_async_session

from .models import Client
from .dependecies import Order, OrderReadSchema
from .schemas import ClientCreateSchema, ClientReadSchema, ClientUpdateSchema

router = APIRouter(tags=["clients"], prefix="/clients")

@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) создание клиента
async def create_client(client: ClientCreateSchema, session=Depends(get_async_session)) -> ClientReadSchema:  #
    statement = insert(Client).values(
        name=client.name,
        rating=client.rating
    ).returning(Client)
    result = await session.scalar(statement)
    await session.commit()
    return result


@router.get("/", status_code=status.HTTP_202_ACCEPTED)  # 2) Получение данных о всех клиентах
async def get_client(session=Depends(get_async_session)) -> list[ClientReadSchema]:
    statement = select(Client)
    result = await session.scalars(statement)
    return list(result)


@router.get("/{client_id}", status_code=status.HTTP_202_ACCEPTED)  # 3) Получение данных о клиенте по id
async def get_client_by_id(client_id: int, session=Depends(get_async_session)) -> ClientReadSchema:
    statement = select(Client).where(Client.id == client_id)  # where - где
    result = await session.scalar(statement)  # await - ожидать
    return result


@router.get("/{client_id}/orders", status_code=status.HTTP_200_OK)  # выводит список заказов клиента
async def get_client_orders(client_id: int, session=Depends(get_async_session)) -> list[OrderReadSchema]:
    statement = select(Order).where(Order.client_id == client_id)
    result = await session.scalars(statement)
    return result



@router.delete("/{client_id}", status_code=status.HTTP_204_NO_CONTENT)  # 4) Удаление клиента по id
async def delete_client_by_id(client_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Client).where(Client.id == client_id)
    await session.execute(statement)
    await session.commit()


@router.put("/{client_id}", status_code=status.HTTP_200_OK)  # 5) Обновление данных клиента по id
async def update_client_by_id(client_id: int, client: ClientUpdateSchema,
                              session=Depends(get_async_session)) -> ClientReadSchema:
    statement = update(Client).where(Client.id == client_id).values(
        name=client.name,
        rating=client.rating
    ).returning(Client)
    result = await session.scalar(statement)
    await session.commit()
    return result


