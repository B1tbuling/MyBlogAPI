from fastapi import HTTPException

from posts.repo import PostRepo


async def get_all_posts():
    return await PostRepo().get_list()


async def get_one_post(id):
    if post := await PostRepo().get_one(id):
        return post
    raise HTTPException(404)


async def create_post(title, text):
    return await PostRepo().create(title, text)


async def update_post(id, title, text):
    if not await PostRepo().get_one(id):
        raise HTTPException(404)
    return await PostRepo().update(id, title, text)


async def delete_post(id):
    if not await PostRepo().get_one(id):
        raise HTTPException(404)
    return await PostRepo().delete(id)



