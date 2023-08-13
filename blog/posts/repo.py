from sqlalchemy import delete, insert, select, update
from sqlalchemy.orm import joinedload
from sqlalchemy.sql.functions import now
from utils.db import get_async_db

from .models import CommentPost, Post
from .schemas import CommentDataSchema, CommentSchema, PostDataSchema, PostSchema


class PostRepo:
    async def create(self, post: PostDataSchema, user_id: int) -> PostDataSchema:
        session = await get_async_db()
        async with session.begin():
            query = (
                insert(Post)
                .values(title=post.title, text=post.text, user_id=user_id)
                .returning(Post)
            )

            result = await session.execute(query)
            return PostSchema.from_orm(result.scalar())

    async def get_list(self) -> list[PostSchema]:
        session = await get_async_db()
        query = select(Post)
        result = await session.execute(query)
        return [PostSchema.from_orm(post) for post in result.scalars().all()]

    async def get_one(self, id: int) -> PostSchema | None:
        session = await get_async_db()
        query = select(Post).where(Post.id == id)
        result = await session.execute(query)
        return PostSchema.from_orm(result.scalar())

    async def update(self, id: int, post: PostDataSchema) -> PostSchema:
        session = await get_async_db()
        async with session.begin():
            query = (
                update(Post)
                .values(title=post.title, text=post.text)
                .where(Post.id == id)
                .returning(Post)
            )

            result = await session.execute(query)
            return PostSchema.from_orm(result.scalar())

    async def delete(self, id: int) -> None:
        session = await get_async_db()
        async with session.begin():
            query = delete(Post).where(Post.id == id)
            await session.execute(query)


class CommentRepo:
    async def create(self, post_id: int, comment: CommentDataSchema, user_id: int) -> CommentSchema:
        session = await get_async_db()
        async with session.begin():
            query = (
                insert(CommentPost)
                .values(text=comment.text, post_id=post_id, user_id=user_id)
                .returning(CommentPost.id)
            )
            result = await session.execute(query)
            return result.scalar()

    async def get_one(self, comment_id: int) -> CommentSchema:
        session = await get_async_db()
        query = (
            select(CommentPost)
            .options(joinedload(CommentPost.user))
            .where(CommentPost.id == comment_id)
        )
        result = await session.execute(query)
        return CommentSchema.from_orm(result.scalar())

    async def get_list(self, post_id: int) -> list[CommentSchema]:
        session = await get_async_db()
        query = (
            select(CommentPost)
            .options(joinedload(CommentPost.user))
            .where(CommentPost.post_id == post_id)
        )
        result = await session.execute(query)
        return [CommentSchema.from_orm(item) for item in result.scalars().all()]

    async def update(self, comment_id: int, comment: CommentDataSchema) -> None:
        session = await get_async_db()
        async with session.begin():
            query = update(CommentPost) \
                .values(text=comment.text, update_time=now()) \
                .where(CommentPost.id == comment_id)

            await session.execute(query)

    async def delete(self, comment_id: int) -> None:
        session = await get_async_db()
        async with session.begin():
            query = delete(CommentPost).where(CommentPost.id == comment_id)
            await session.execute(query)
