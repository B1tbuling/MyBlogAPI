from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers

from . import auth, manager, models, schemas, services


auth_router = APIRouter(prefix="/auth", tags=["auth"])
user_router = APIRouter(prefix="/users", tags=["users"])


fastapi_users = FastAPIUsers[models.User, int](manager.get_user_manager,[auth.auth_backend])
current_user = fastapi_users.current_user()


auth_router.include_router(fastapi_users.get_auth_router(auth.auth_backend), prefix="/jwt", tags=["auth"])
auth_router.include_router(fastapi_users.get_register_router(schemas.UserRead, schemas.UserCreate))
auth_router.include_router(fastapi_users.get_reset_password_router())
auth_router.include_router(fastapi_users.get_verify_router(schemas.UserRead))


@user_router.get("/profile", response_model=schemas.UserProfileInfo)
async def get_user_pofile(user=Depends(current_user)):
    print(user.__dict__)
    return await services.get_profile_info(user)


# user_router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate))
