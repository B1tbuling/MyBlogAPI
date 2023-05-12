from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from posts.routes import router as post_router
from users.routes import auth_router, user_router


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post_router)
app.include_router(auth_router)
app.include_router(user_router)

