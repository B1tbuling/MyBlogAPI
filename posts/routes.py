from fastapi import APIRouter, Depends

from users.routes import current_user, fastapi_users
from .schemas import PostData, PostBaseData, CommentsSchemas, CommentCreate
from .services import *

router = APIRouter()


@router.get("/posts", response_model=list[PostData])
async def get_posts():
    return await get_all_posts()


@router.get("/posts/{id}", response_model=PostData)
async def get_post(id: int):
    return await get_one_post(id)


@router.post("/posts/create")
async def create_posts(post: PostBaseData, user=Depends(current_user)):
    return await create_post(post.title, post.text, user)


@router.post("/posts/update/{id}")
async def update_posts(id: int, post: PostBaseData, user=Depends(current_user)):
    return await update_post(id, post.title, post.text, user)


@router.delete("/posts/delete/{id}")
async def delete_posts(id: int, user=Depends(current_user)):
    return await delete_post(id, user)


@router.get("/posts/{id}/comments", response_model=list[CommentsSchemas])
async def get_comments(id: int):
    return await get_comments_list(id)


@router.post("/posts/{id}/comments/create")
async def create_comment(comment: CommentCreate, id: int, user=Depends(current_user)):
    return await create_comment(id, comment.text, user)

