from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text, DateTime, MetaData
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from sqlalchemy.sql.functions import now

connection = "postgresql://username:1234@localhost/blog"
engine = create_engine(connection)
Base = declarative_base()


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(60), nullable=False)
    text = Column(Text, nullable=False)
    date = Column(DateTime, server_default='now()', default=now())
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