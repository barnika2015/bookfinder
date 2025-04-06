from pymongo import MongoClient

class Database:
    def __init__(self):
        self._client = MongoClient('mongodb://localhost:27017/')
        self._db = self._client['BooksDB']
        self._collection = self._db['books_collection']

    def add_book(self, book):
        self._collection.insert_one(book.as_dict())
   
    def find_book(self, title):
        return self._collection.find_one({"title": title})
    
    