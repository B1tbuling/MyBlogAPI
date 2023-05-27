from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers

from users.auth import auth_backend
from users.manager import get_user_manager
from users.models import User
from users.schemas import *
from users.services import get_profile_info


auth_router = APIRouter(prefix="/auth", tags=["auth"])
user_router = APIRouter(prefix="/users", tags=["users"])


fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend],)
current_user = fastapi_users.current_user()


auth_router.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/jwt", tags=["auth"])
auth_router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))
auth_router.include_router(fastapi_users.get_reset_password_router())
auth_router.include_router(fastapi_users.get_verify_router(UserRead))


@user_router.get("/profile", response_model=UserProfileInfo)
async def get_user_pofile(user=Depends(current_user)):
    print(user.__dict__)
    return await get_profile_info(user)

# user_router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate))