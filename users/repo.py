from fastapi import HTTPException
from sqlalchemy import select, insert, update, delete

from users.models import User
from utils.db import get_async_db


class UserRepo:
    async def get_profile(self, user):
        session = await get_async_db()
        query = select(User).where(User.id == user.id)
        result = await session.execute(query)
        print(result)
        user = result.scalar()
        print(user.id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
