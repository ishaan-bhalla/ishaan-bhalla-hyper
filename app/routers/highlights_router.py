from fastapi import APIRouter
from app.controllers.highlights_controller import fetch_highlights

router = APIRouter()

@router.get("/highlights", tags=["Highlights"])
def get_highlights():
    """
    API endpoint to fetch soccer highlights.
    """
    return fetch_highlights()
