import pickle

# Domain entity class
# Domain entity class
class Book:
    def __init__(self, isbn, author, title):
        self.isbn = isbn
        self.author = author
        self.title = title


    def set_books(self, new_books):
        # Set the state of the books to the given list
        self.books = new_books

    def __str__(self):
        return f"ISBN: {self.isbn}, Author: {self.author}, Title: {self.title}"