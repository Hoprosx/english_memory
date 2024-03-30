from sqlalchemy import select, insert
from fastapi import HTTPException, status
from ..database.database import session


class BaseDao:
    model = None

    @classmethod
    async def get_all_word(cls, **filter_by):
        async with session() as s:
            query = select(cls.model).filter_by(**filter_by)
            result = await s.execute(query)
            return result.scalars().all()

