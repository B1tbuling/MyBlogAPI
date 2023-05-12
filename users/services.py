from users.repo import UserRepo


async def get_profile_info(user):
    return await UserRepo().get_profile(user)
