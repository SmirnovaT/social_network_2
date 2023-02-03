from fastapi import Depends, APIRouter


from src.services.post import PostService

post_router = APIRouter(
    prefix="/api/post", tags=["post"], responses={404: {"description": "Not found"}}
)


@post_router.get("/")
async def read_all(service: PostService = Depends(PostService)):
    pass