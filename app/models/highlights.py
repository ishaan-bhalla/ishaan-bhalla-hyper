from pydantic import BaseModel

class Highlight(BaseModel):
    minute: int
    event: str
