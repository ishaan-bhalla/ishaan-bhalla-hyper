from app.services.highlights_service import get_mock_highlights

def fetch_highlights():
    """
    Fetch soccer highlights using the service logic.
    """
    highlights = get_mock_highlights()
    return {"highlights": highlights}
