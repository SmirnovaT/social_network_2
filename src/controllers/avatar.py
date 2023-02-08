import json

from fastapi import File, UploadFile, APIRouter
from minio import Minio

client = Minio(endpoint="play.min.io", secure=True, secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
               access_key="Q3AM3UQ867SPQQA43P2F")

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
    result = client.put_object("tanyatrip", file.filename, data, size)

    return result
