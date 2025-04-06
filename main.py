from fastapi import FastAPI
from app import MyLibrary
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/search")
async def search_books(search_term: str):
    print(f"Searching for books with term: {search_term}")
    results = MyLibrary.search_books(search_term)
    return {"search_term": search_term, "results": str([str(book) for book in results])}