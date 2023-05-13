from fastapi import HTTPException
from posts.repo import PostRepo, CommentRepo

from posts.models import CommentPost
from posts.schemas import CommentSchema, CommentDataSchema, PostDataSchema, PostSchema
from users.models import User


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
    elif exist_post.user_id != user.id:
        raise HTTPException(403, detail="This post cannot be edited by this user")
    return await PostRepo().update(id=id, post=post)


async def delete_post(id: int, user: User) -> None:
    post = await PostRepo().get_one(id)
    if not post:
        raise HTTPException(404)
    elif post.user_id != user.id:
        raise HTTPException(403, detail="This post cannot be deleted by this user")
    await PostRepo().delete(id=id)


# Comments

async def create_comment(post_id: int, comment: CommentDataSchema, user: User) -> CommentPost:
    return await CommentRepo().create(post_id=post_id, comment=comment, user_id=user.id)


async def get_comments_list(post_id: int) -> list[CommentSchema]:
    return await CommentRepo().get_list(post_id=post_id)
