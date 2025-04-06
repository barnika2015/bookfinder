from fastapi import FastAPI
from app import Library
from fastapi.middleware.cors import CORSMiddleware

MyLibrary = None




async def lifespan(app: FastAPI):
    # This code runs when the app starts
    print("App is starting...")
    global MyLibrary
    MyLibrary = Library()
    MyLibrary.import_books('books.csv') 

    # Yield control to FastAPI to run the app
    yield

    # This code runs when the app is shutting down
    print("App is shutting down...")

app = FastAPI(lifespan=lifespan)

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

