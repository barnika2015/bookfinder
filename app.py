from database import Database  
from book import Book
class Library:
    def __init__(self):
        self._db = Database()

    def import_books(self, filepath):
        with open(filepath, 'r') as file:
            for line in file:
                title, author, year = line.strip().split(',')
         ##       self.books.append(Book(title, author, int(year)))
                book = Book(title, author, int(year))
                self._db.add_book(book)
                print(f"Book added to database: {book}")


    def list_books(self):
        return [str(book) for book in self.books]
    
    def search_books(self, search_term):
        found=[]
        if not search_term:
            return found
        for book in self._db.find_books(search_term):
            found.append(book)
        return found

           

if __name__ == "__main__":
    library = Library()
    library.import_books('books.csv') 



