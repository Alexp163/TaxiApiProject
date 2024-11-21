from sqlalchemy import select, update

from database import AsyncSession, Base

async def increase_wallet(table: Base, price: float, session: AsyncSession, ratio: float, common_id: int):
    statement = select(table).where(table.id == common_id)
    common = await session.scalar(statement)
    wallet = common.wallet + (price * ratio)
    statement = update(table).where(table.id == common_id).values(
        wallet=wallet
    )
    await session.execute(statement)