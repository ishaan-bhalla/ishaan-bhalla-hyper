from fastapi import FastAPI
from app.routers.highlights_router import router as highlights_router

app = FastAPI(title="Soccer Highlights API")

# Register the highlights router
app.include_router(highlights_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Soccer Highlights API!"}
