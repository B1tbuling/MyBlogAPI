from fastapi import APIRouter

from .schemas import PostData, PostBaseData
from .services import *

router = APIRouter()


@router.get("/posts", response_model=list[PostData])
async def get_posts():
    return await get_all_posts()


@router.get("/posts/{id}", response_model=PostData)
async def get_post(id: int):
    return await get_one_post(id)


@router.post("/posts/create")
async def create_posts(post: PostBaseData):
    return await create_post(post.title, post.text)


@router.post("/posts/update/{id}")
async def update_posts(id: int, post: PostBaseData):
    return await update_post(id, post.title, post.text)


@router.delete("/posts/delete/{id}")
async def delete_posts(id: int):
    return await delete_post(id)
