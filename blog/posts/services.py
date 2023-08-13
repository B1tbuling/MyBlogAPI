from fastapi import HTTPException
from users.models import User

from .models import CommentPost
from .repo import CommentRepo, PostRepo
from .schemas import CommentDataSchema, CommentSchema, PostDataSchema, PostSchema


async def create_post(post: PostDataSchema, user: User) -> PostDataSchema:
    return await PostRepo().create(post=post, user_id=user.id)


async def get_all_posts() -> list[PostSchema]:
    return await PostRepo().get_list()


async def get_one_post(id: int) -> PostSchema:
    if post := await PostRepo().get_one(id=id):
        return post
    raise HTTPException(404, detail="Posts not found")


async def update_post(id: int, post: PostDataSchema, user: User) -> PostSchema:
    exist_post = await PostRepo().get_one(id)
    if not exist_post:
        raise HTTPException(404)
    if exist_post.user_id != user.id:
        raise HTTPException(403, detail="This post cannot be edited by this user")
    return await PostRepo().update(id=id, post=post)


async def delete_post(id: int, user: User) -> None:
    post = await PostRepo().get_one(id)
    if not post:
        raise HTTPException(404)
    if post.user_id != user.id:
        raise HTTPException(403, detail="This post cannot be deleted by this user")
    await PostRepo().delete(id=id)


# Comments


async def create_comment(post_id: int, comment: CommentDataSchema, user: User) -> CommentPost:
    return await CommentRepo().create(post_id=post_id, comment=comment, user_id=user.id)


async def get_comments_list(post_id: int) -> list[CommentSchema]:
    return await CommentRepo().get_list(post_id=post_id)


async def update_comment(comment_id: int, comment: CommentDataSchema, user: User) -> None:
    comment_before_update = await CommentRepo().get_one(comment_id)
    if not comment_before_update:
        raise HTTPException(404)
    if comment_before_update.user.id != user.id:
        raise HTTPException(403, detail="This comment cannot be updated by this user")
    await CommentRepo().update(comment_id=comment_id, comment=comment)


async def delete_comment(comment_id: int, user: User) -> None:
    comment = await CommentRepo().get_one(comment_id)
    if not comment:
        raise HTTPException(404)
    if comment.user.id != user.id:
        raise HTTPException(403, detail="This comment cannot be deleted by this user")
    await CommentRepo().delete(comment_id=comment_id)
