from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from utils.db import get_async_db


class BaseRepo:
    def __init__(self, session: AsyncSession = get_async_db()):
        self.session = session
