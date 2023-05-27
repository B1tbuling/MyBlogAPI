from fastapi import APIRouter, Depends

from users.routes import current_user

from .services import *


router = APIRouter()


@router.post("/posts", status_code=201, response_model=PostSchema)
async def create_posts(post: PostDataSchema, user=Depends(current_user)):
    print(user.id)
    return await create_post(post=post, user=user)


@router.get("/posts", response_model=list[PostSchema])
async def get_posts():
    return await get_all_posts()


@router.get("/posts/{id}", response_model=PostSchema)
async def get_post(id: int):
    return await get_one_post(id=id)


@router.put("/posts/{id}", response_model=PostSchema)
async def update_posts(id: int, post: PostDataSchema, user=Depends(current_user)):
    return await update_post(id=id, post=post, user=user)


@router.delete("/posts/{id}", status_code=204)
async def delete_posts(id: int, user=Depends(current_user)):
    await delete_post(id=id, user=user)


# Comments

@router.post("/posts/{post_id}/comments", status_code=201)
async def create_comment(comment: CommentDataSchema, post_id: int, user=Depends(current_user)):
    return await create_comment(post_id=post_id, comment=comment, user=user)


@router.get("/posts/{post_id}/comments", response_model=list[CommentSchema])
async def get_comments(post_id: int):
    return await get_comments_list(post_id=post_id)
