from fastapi import FastAPI

from database import Base, engine
from src.controllers.auth import auth_router
from src.controllers.avatar import avatar_router
from src.controllers.post import post_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(post_router)
app.include_router(auth_router)
app.include_router(avatar_router)