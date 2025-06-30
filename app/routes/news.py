from fastapi import APIRouter
from app.services.news import get_latest_news

router = APIRouter()

@router.get("/")
def news():
    return {"headlines": get_latest_news()}

