from fastapi import HTTPException
from sqlalchemy import select, insert, update, delete

from utils.db import get_async_db

from posts.models import Post


class PostRepo:
    async def get_one(self, id):
        session = await get_async_db()
        query = select(Post).where(Post.id == id)
        result = await session.execute(query)
        post = result.scalar()
        if post is None:
            raise HTTPException(status_code=404, detail="Post not found")
        return post

        # post = await session.query(Post).filter(Post.id == id).first_async()
        # if post is None:
        #     raise HTTPException(status_code=404, detail="Post not found")
        # return post

    async def get_list(self):
        session = await get_async_db()
        query = select(Post)
        result = await session.execute(query)
        posts = result.scalars().all()
        print(posts)
        if not posts:
            raise HTTPException(status_code=404, detail="Posts not found")
        return posts

    async def create(self, title, text):
        session = await get_async_db()
        # post = Post(title=title, text=text)
        # session.add(post)
        # await session.commit()
        # await session.refresh(post)
        # return post.id

        async with session.begin():
            query = insert(Post).values(title=title, text=text).returning(Post.id)
            print(query)
            result = await session.execute(query)
            # return result.one() # (5,)
            return result.scalar() # 5

    async def update(self, id, title, text):
        session = await get_async_db()
        async with session.begin():
            query = update(Post).values(title=title, text=text).where(Post.id == id).returning(Post.id)
            result = await session.execute(query)
            return result.scalar()

        #session = await get_async_db()
        # post = Post(id=10, title='dfdf', text='dfdf')
        # session.add(post)
        # post = session.add(Post).filter(Post.id == id).first()
        # post.title, post.text = title, text
        # session.commit()
        # session.refresh(post)
        # return post

    async def delete(self, id):
        session = await get_async_db()
        async with session.begin():
            query = delete(Post).where(Post.id == id)
            await session.execute(query)
            return {"message": "Post deleted successfully."}

        # session = await get_async_db()
        # post = session.query(Post).filter(Post.id == id).first_async()
        # session.delete(post)
        # await session.commit()
        # return {"message": "User deleted successfully."}