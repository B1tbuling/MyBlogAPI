from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from posts.routes import router as post_router

from fastapi_users import FastAPIUsers


from users.cookie import auth_backend
from users.manager import get_user_manager
from users.models import User
from users.schemas import UserRead, UserCreate

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post_router)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

