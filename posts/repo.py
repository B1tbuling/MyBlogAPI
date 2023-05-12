from fastapi import HTTPException
from sqlalchemy import select, insert, update, delete

from posts.schemas import CommentsRead
from users.models import User
from users.schemas import UserProfileInfo
from utils.db import get_async_db

from posts.models import Post, CommentPost


class PostRepo:
    async def get_one(self, id: int) -> Post:
        session = await get_async_db()
        query = select(Post).where(Post.id == id)
        result = await session.execute(query)
        post = result.scalar()
        print(post.user_id)
        if post is None:
            raise HTTPException(status_code=404, detail="Post not found")
        return post

    async def get_list(self) -> list[Post]:
        session = await get_async_db()
        query = select(Post)
        result = await session.execute(query)
        posts = result.scalars().all()
        if not posts:
            raise HTTPException(status_code=404, detail="Posts not found")
        return posts

    async def create(self, title: str, text: str, user: User) -> Post:
        session = await get_async_db()
        async with session.begin():
            query = insert(Post).values(title=title, text=text, user_id=user.id).returning(Post.id)
            result = await session.execute(query)
            return result.scalar()

    async def update(self, id: int, title: str, text: str) -> Post:
        session = await get_async_db()
        async with session.begin():
            query = update(Post).values(title=title, text=text).where(Post.id == id).returning(Post.id)
            result = await session.execute(query)
            return result.scalar()

    async def delete(self, id: int):
        session = await get_async_db()
        async with session.begin():
            query = delete(Post).where(Post.id == id)
            await session.execute(query)
            return {"message": "Post deleted successfully."}


class CommentRepo:
    async def get_list(self, id: int) -> list[CommentsRead]:
        session = await get_async_db()
        # async with session.begin():
        query = select(CommentPost, User.first_name, User.last_name, User.username). \
            join(User, CommentPost.user_id == User.id).where(CommentPost.post_id == id)
        result = await session.execute(query)
        data = result.all()
        comment_list = []
        for item in data:
            comment_list.append(
                CommentsRead(
                    id=item[0].id,
                    text=item[0].text,
                    user=UserProfileInfo(
                        first_name=item[1],
                        last_name=item[2],
                        username=item[3]
                    )
                )
            )
        return comment_list

    async def create(self, id: int, text: str, user: User) -> Post:
        session = await get_async_db()
        async with session.begin():
            query = insert(CommentPost).values(text=text, post_id=id, user_id=user.id).returning(CommentPost.id)
            print(query)
            result = await session.execute(query)
            return result.scalar()