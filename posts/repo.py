from fastapi import HTTPException
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import joinedload

from posts.schemas import CommentsSchemas
from users.models import User
from users.schemas import UserProfileInfo
from utils.base_repo import BaseRepo

from posts.models import Post, CommentPost


class PostRepo(BaseRepo):
    async def get_one(self, id: int) -> Post:
        query = select(Post).where(Post.id == id)
        result = await self.session.execute(query)
        return result.scalar()

    async def get_list(self) -> list[Post]:
        query = select(Post)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def create(self, title: str, text: str, user: User) -> Post:
        async with self.session.begin():
            query = insert(Post) \
                .values(title=title, text=text, user_id=user.id) \
                .returning(Post.id)

            result = await self.session.execute(query)
            return result.scalar()

    async def update(self, id: int, title: str, text: str) -> Post:
        async with self.session.begin():
            query = update(Post) \
                .values(title=title, text=text) \
                .where(Post.id == id) \
                .returning(Post.id)

            result = await self.session.execute(query)
            return result.scalar()

    async def delete(self, id: int):
        async with self.session.begin():
            query = delete(Post).where(Post.id == id)
            await self.session.execute(query)
            return {"message": "Post deleted successfully."}


class CommentRepo(BaseRepo):
    async def get_list(self, post_id: int) -> list[CommentsSchemas]:
        query = select(CommentPost) \
            .options(joinedload(CommentPost.user)) \
            .where(CommentPost.post_id == post_id)

        result = await self.session.execute(query)
        return [CommentsSchemas.from_orm(item) for item in result.scalars().all()]

    async def create(self, post_id: int, text: str, user: User) -> Post:
        async with self.session.begin():
            query = insert(CommentPost).values(text=text, post_id=post_id, user_id=user.id).returning(CommentPost.id)
            print(query)
            result = await self.session.execute(query)
            return result.scalar()
