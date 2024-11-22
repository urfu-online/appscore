from fastapi import  FastAPI
from .utils import calculate_file_hash_by_url, calculate_filestorage_hash_by_url

cdn_app = FastAPI()


@cdn_app.get("/")
async def root(url: str | None):
    if url:
        file_hash = calculate_file_hash_by_url(url)
        filestorage_hash = calculate_filestorage_hash_by_url(url)
        return {"file_hash": file_hash, "filestorage_hash": filestorage_hash}
    
    return {"message": "Анус себе захэшируй, ПИДОР"}

@cdn_app.get("/{hash}")
async def get_hash(hash: str):
    return {"hash": hash}