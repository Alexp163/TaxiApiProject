from fastapi import APIRouter, status, Depends
from sqlalchemy import insert, select, delete, update

from database import get_async_session
from .models import Category
from .schemas import CategoryCreateSchema, CategoryReadSchema, CategoryUpdateSchema

router = APIRouter(tags=["categories"], prefix="/categories")

# fmt: off
@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) Создание категории
async def create_category(category: CategoryCreateSchema, session=Depends(get_async_session)) -> CategoryReadSchema:
    statement = insert(Category).values(
        title=category.title,
        schedule=category.schedule
    ).returning(Category)
    result = await session.scalar(statement)
    await session.commit()
    return result
# fmt: on

@router.get("/", status_code=status.HTTP_202_ACCEPTED)  # 2) Получение данных о всех категориях
async def get_categories(session=Depends(get_async_session)) -> list[CategoryReadSchema]:
    statement = select(Category)
    result = await session.scalars(statement)
    return list(result)


@router.get("/category_id", status_code=status.HTTP_202_ACCEPTED)  # 3) Получение данных о категории по id
async def get_category_by_id(category_id: int, session=Depends(get_async_session)) -> CategoryReadSchema:
    statement = select(Category).where(Category.id == category_id)
    result = await session.scalar(statement)
    return result


@router.delete("/category_id", status_code=status.HTTP_204_NO_CONTENT)  # 4) Удаление категории по id
async def delete_category_by_id(category_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Category).where(Category.id == category_id)
    await session.execute(statement)
    await session.commit()

# fmt: off
@router.put("/category_id", status_code=status.HTTP_200_OK)  # 5) Обновление категории по id
async def update_category_by_id(category_id: int, category: CategoryUpdateSchema,
                                session=Depends(get_async_session)) -> CategoryReadSchema:
    statement = update(Category).where(Category.id == category_id).values(
        title=category.title,
        schedule=category.schedule
    ).returning(Category)
    result = await session.scalar(statement)
    await session.commit()
    return result
# fmt: on