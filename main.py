from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db_execute.db_execute_post import create_post_db, get_one_post_db, get_all_posts_db, update_post_db, delete_post_db
from schemas import PostData, PostBaseData

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/posts", response_model=List[PostData])
async def get_posts():
    return get_all_posts_db()


@app.get("/posts/{id}", response_model=PostData)
async def get_post(id: int):
    return get_one_post_db(id)


@app.post("/posts/create")
async def create_posts(post: PostData):
    return create_post_db(post.title, post.text)


@app.post("/posts/update/{id}")
async def update_posts(id: int, post: PostBaseData):
    return update_post_db(id, post.title, post.text)


@app.delete("/posts/delete/{id}")
async def delete_posts(id: int):
    return delete_post_db(id)


