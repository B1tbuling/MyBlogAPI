from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

import config

engine = create_engine(config.DataBaseConfig.URL, echo=True)
async_engine = create_async_engine(config.DataBaseConfig.ASYNC_URL, echo=True)
Base = declarative_base()

async_session = sessionmaker(bind=async_engine, class_=AsyncSession)


async def get_async_db():
    async with async_session() as session:
        return session
