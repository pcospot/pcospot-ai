import os
from fastapi import APIRouter
from dotenv import load_dotenv
import services.vectorSearch as vs

load_dotenv()

router = APIRouter(
    prefix="/search"
)

@router.get('/search')
async def search(query: str = "", limit: int = 30, filter: str = "") -> list:
    return vs.search(query, limit, filter)