from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_NAME = os.environ.get("DB_NAME")

# sqlalchemy.url = postgresql://%(DB_USER)s:%(DB_PASS)s@localhost/%(DB_NAME)s

