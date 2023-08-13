import os


os.environ["DB_NAME"] = "test_blog"


from config import DataBaseConfig
from posts import *


print(DataBaseConfig.URL)
