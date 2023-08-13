import config
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base


# engine = create_engine(config.DataBaseConfig.URL, echo=False)
# async_engine = create_async_engine(config.DataBaseConfig.ASYNC_URL, echo=False)

engine = create_engine(config.TestDataBaseConfig.URL, echo=False)
async_engine = create_async_engine(config.TestDataBaseConfig.ASYNC_URL, echo=False)


Base = declarative_base()

async_session = async_sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False
)


async def get_async_db() -> AsyncSession:
    async with async_session() as session:
        return session
