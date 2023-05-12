from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import now

from utils.db import Base


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(60), nullable=False)
    text = Column(Text, nullable=False)
    date_create = Column(DateTime, server_default='now()', default=now())
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", backref='posts')
    tags = relationship(
        "Tags",
        secondary="posts_tags",
        backref="posts"
    )


class Tags(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(60), nullable=False)


class AssociationPostTags(Base):
    __tablename__ = 'posts_tags'

    post_id = Column(Integer, ForeignKey('post.id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tag.id'), primary_key=True)


class CommentPost(Base):
    __tablename__ = 'comment_post'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text, nullable=False)
    date_create = Column(DateTime, server_default='now()', default=now())
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship("Post", backref='comments')
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", backref='comments')
