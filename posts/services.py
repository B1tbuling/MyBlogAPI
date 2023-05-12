from fastapi import HTTPException
from posts.repo import PostRepo, CommentRepo

from posts.models import Post, CommentPost
from posts.schemas import CommentsSchemas
from users.models import User


async def get_one_post(id: int) -> Post:
    if post := await PostRepo().get_one(id):
        return post
    raise HTTPException(404, detail="Posts not found")


async def get_all_posts() -> list[Post]:
    return await PostRepo().get_list()


async def create_post(title: str, text: str, user: User) -> Post:
    return await PostRepo().create(title, text, user)


async def update_post(id: int, title: str, text: str, user: User) -> Post:
    post = await PostRepo().get_one(id)
    if not post:
        raise HTTPException(404)
    elif post.user_id != user.id:
        raise HTTPException(403, detail="This post cannot be edited by this user")
    return await PostRepo().update(id, title, text)


async def delete_post(id: int, user: User):
    post = await PostRepo().get_one(id)
    if not post:
        raise HTTPException(404)
    elif post.user_id != user.id:
        raise HTTPException(403, detail="This post cannot be deleted by this user")
    return await PostRepo().delete(id)


async def get_comments_list(id: int) -> list[CommentsSchemas]:
    return await CommentRepo().get_list(id)


async def create_comment(id: int, text: str, user: User) -> CommentPost:
    return await CommentRepo().create(id, text, user)