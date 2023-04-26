import os
from dotenv import load_dotenv


load_dotenv()


class DataBaseConfig:
    USER = os.getenv("DB_USER")
    PASS = os.getenv("DB_PASS")
    PORT = os.getenv("DB_PORT")
    HOST = os.getenv("DB_HOST")
    NAME = os.getenv("DB_NAME")
    pg_driver = 'asyncpg'

    ASYNC_URL = f"postgresql+{pg_driver}://{USER}:{PASS}@localhost/{NAME}"
    URL = f"postgresql://{USER}:{PASS}@localhost/{NAME}"


class JWTConfig:
    SECRET = os.getenv("SECRET")



