# from fastapi import HTTPException
#
# from sqlalchemy.orm import Session
#
#
# class BaseRepo:
#     def get_one(self, id): ...
#     def get_list(self): ...
#     def create(self, title, text): ...
#     def update(self, id, title, text): ...
#     def delete(self, id): ...
#
#
# class EntityRepo(BaseRepo):
#
#     entity: ... = None
#
#     def get_one(self, id):
#         with Session() as session:
#             post = session.query(self.entity).filter(self.entity.id == id).first()
#             if post is None:
#                 raise HTTPException(status_code=404, detail="self.entity not found")
#             return post
#
#     def get_list(self):
#         with Session() as session:
#             posts = session.query(self.entity).all()
#             if posts is None:
#                 raise HTTPException(status_code=404, detail="self.entitys not found")
#             return posts
#
#     def create(self, title, text):
#         with Session() as session:
#             session.add(self.entity(title=title, text=text))
#             session.commit()
#
#     def update(self, id, title, text):
#         with Session() as session:
#             post = session.query(self.entity).filter(self.entity.id == id).first()
#             post.title, post.text = title, text
#             session.commit()
#             session.refresh(post)
#             return post
#
#     def delete(self, id):
#         with Session() as session:
#             post = session.query(self.entity).filter(self.entity.id == id).first()
#             session.delete(post)
#             session.commit()
#             return {"message": "User deleted successfully."}