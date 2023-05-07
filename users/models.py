from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime

from utils.db import Base, async_session


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, nullable=False, primary_key=True)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)