from blog.utils.db import get_async_db


class BaseRepo:
    def __init__(self):
        self.session = get_async_db()
