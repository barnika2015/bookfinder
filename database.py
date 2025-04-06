from pymongo import MongoClient
from book import Book
class Database:
    def __init__(self):
        self._client = MongoClient('mongodb://localhost:27017/')
        self._db = self._client['BooksDB']
        self._collection = self._db['books_collection']

    def add_book(self, book):
        self._collection.insert_one(book.as_dict())
   
    def find_books(self, query):
        find_term = {
            "$or": [
                {"title": {"$regex": query, "$options": "i"}},  # Substring match in title (case-insensitive)
                {"author": {"$regex": query, "$options": "i"}}  # Substring match in author (case-insensitive)
            ]
        }
        for result in self._collection.find(find_term):
            yield Book(result['title'], result['author'], result['year'], result['publisher'])
    
    