from fastapi import HTTPException

from db import *


Session = sessionmaker(bind=engine)


def get_one_post_db(id):
    with Session() as session:
        post = session.query(Post).filter(Post.id == id).first()
        if post is None:
            raise HTTPException(status_code=404, detail="Post not found")
        return post


def get_all_posts_db():
    with Session() as session:
        posts = session.query(Post).all()
        if posts is None:
            raise HTTPException(status_code=404, detail="Posts not found")
        return posts


def create_post_db(title, text):
    with Session() as session:
        session.add(Post(title=title, text=text))
        session.commit()


def update_post_db(id, title, text):
    with Session() as session:
        post = session.query(Post).filter(Post.id == id).first()
        post.title, post.text = title, text
        session.commit()
        session.refresh(post)
        return post


def delete_post_db(id):
    with Session() as session:
        post = session.query(Post).filter(Post.id == id).first()
        session.delete(post)
        session.commit()
        return {"message": "User deleted successfully."}




