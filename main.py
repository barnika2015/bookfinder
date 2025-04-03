from fastapi import FastAPI
from app import MyLibrary

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/search")
async def search_books(search_term: str):
    results = MyLibrary.search_books(search_term)
    return {"search_term": search_term, "results": [str(book) for book in results]}