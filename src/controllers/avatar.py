from io import BytesIO

from fastapi import File, UploadFile, APIRouter
from minio import Minio

client = Minio(endpoint="minio:9000", secure=False, access_key="dkfsdfj123j2143jlkl",
               secret_key="gergrthrth56456456")

avatar_router = APIRouter(
    prefix="/api/avatar",
    tags=["avatar"],
    responses={401: {"user": "Not authorized"}},
)


@avatar_router.post("/")
async def index(file: UploadFile = File(...)):
    found = client.bucket_exists("tanyatrip")
    if not found:
        client.make_bucket("tanyatrip")
    else:
        print("Bucket 'tanyatrip' already exists")
    data = file.file.read()
    size = len(data)
    result = client.put_object("tanyatrip", file.filename, BytesIO(data), size)

    return result
