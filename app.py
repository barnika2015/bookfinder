class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
    
    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.year})"
    
class Library:
    def __init__(self):
        self.books = []

    def import_books(self, filepath):
        with open(filepath, 'r') as file:
            for line in file:
                title, author, year = line.strip().split(',')
                self.books.append(Book(title, author, int(year)))

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def list_books(self):
        return [str(book) for book in self.books]
    
    def search_books(self, search_term):
        found=[]
        for book in self.books:
            if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower():
                found.append(book)
        return found

MyLibrary = Library()
MyLibrary.import_books('books.csv') 



if __name__ == "__main__":
    library = Library()
    library.import_books('books.csv')
    print("Books in the library:")
    for book in library.list_books():
        print(book)
    print("\nSearch for 'Vinci':")
    for book in library.search_books('Vinci'):
        print(book)

