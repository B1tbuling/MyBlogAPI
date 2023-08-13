from fastapi import APIRouter, Depends
from users.routes import current_user

from . import schemas, services


router = APIRouter()


@router.post("/posts", status_code=201, response_model=schemas.PostSchema)
async def create_posts(post: schemas.PostDataSchema, user=Depends(current_user)):
    print(user.id)
    return await services.create_post(post=post, user=user)


@router.get("/posts", response_model=list[schemas.PostSchema])
async def get_posts():
    return await services.get_all_posts()


@router.get("/posts/{id}", response_model=schemas.PostSchema)
async def get_post(id: int):
    return await services.get_one_post(id=id)


@router.put("/posts/{id}", response_model=schemas.PostSchema)
async def update_posts(id: int, post: schemas.PostDataSchema, user=Depends(current_user)):
    return await services.update_post(id=id, post=post, user=user)


@router.delete("/posts/{id}", status_code=204)
async def delete_posts(id: int, user=Depends(current_user)):
    await services.delete_post(id=id, user=user)


# Comments


@router.post("/posts/{post_id}/comments", status_code=201)
async def create_comment(comment: schemas.CommentDataSchema, post_id: int, user=Depends(current_user)):
    return await services.create_comment(post_id=post_id, comment=comment, user=user)


@router.get("/posts/{post_id}/comments", response_model=list[schemas.CommentSchema])
async def get_comments(post_id: int):
    return await services.get_comments_list(post_id=post_id)


@router.put("/posts/comments/{comment_id}", status_code=201)
async def delete_comment(comment_id: int, comment: schemas.CommentDataSchema, user=Depends(current_user)):
    return await services.update_comment(comment_id=comment_id, comment=comment, user=user)


@router.delete("/posts/comments/{comment_id}", status_code=204)
async def update_comment(comment_id: int, user=Depends(current_user)):
    return await services.delete_comment(comment_id=comment_id, user=user)
