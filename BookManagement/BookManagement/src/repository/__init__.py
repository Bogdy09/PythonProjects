import pickle

from src.domain import Book


class MemoryRepository:
    def __init__(self):
        self.books = []
        self.history = []

    def add_book(self, book):
        self.books.append(book)

    def save_state(self):
        """
                Saves the current state of books in the repository to the history.
        """
        # Save the current state of books to history
        self.history.append(list(self.books))

    def undo_last_operation(self):
        """
                Reverts the most recent operation performed on the repository.
                Restores the state of the repository to the previous state stored in history.
        """
        if self.history:
            # Restore the previous state from history
            self.books = self.history.pop()

    def get_books(self):
        """
                Retrieves the list of books from the repository.

                Returns:
                    List of Book objects present in the repository.
        """
        return self.books

class TextFileRepository:
    def __init__(self, file_path, repository):
        self.file_path = file_path
        self.repository = repository

    def add_book(self, book):
        with open(self.file_path, 'a') as file:
            file.write(f"{book.isbn},{book.author},{book.title}\n")

    def filter_books_and_update_file(self, criterion):
        updated_books = []
        with open(self.file_path, 'r') as file:
            for line in file:
                if criterion not in line.split(',')[2]:
                    updated_books.append(line.strip() + '\n')

        with open(self.file_path, 'w') as file:
            file.writelines(updated_books)

    def update_file_from_repository(self):
        updated_books = [f"{book.isbn},{book.author},{book.title}\n" for book in self.repository.get_books()]

        with open(self.file_path, 'w') as file:
            file.writelines(updated_books)

    def save_state(self, books):
        with open(self.file_path, 'w') as file:
            for book in books:
                file.write(f"{book.isbn},{book.author},{book.title}\n")

    def get_books(self):
        books = []
        with open(self.file_path, 'r') as file:
            for line in file:
                isbn, author, title = line.strip().split(',')
                books.append(Book(isbn, author, title))
        return books

class BinaryFileRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def add_book(self, book):
        with open(self.file_path, 'ab') as file:
            pickle.dump(book, file)

    def get_books(self):
        books = []
        try:
            with open(self.file_path, 'rb') as file:
                while True:
                    book = pickle.load(file)
                    books.append(book)
        except EOFError:
            pass
        return books

    def update_file(self, books):
        with open(self.file_path, 'wb') as file:
            for book in books:
                pickle.dump(book, file)

    def filter_books_and_update_file(self, criterion):
        all_books = self.get_books()
        filtered_books = [book for book in all_books if not book.title.startswith(criterion)]
        self.update_file(filtered_books)

    def update_file(self, books):
        """
        Updates the binary file with a list of books.

        Parameters:
            books (list): List of Book objects to be updated in the binary file.
        """
        with open(self.file_path, 'wb') as file:
            for book in books:
                pickle.dump(book, file)

    def save_state(self, books):
        """
        Saves the current state of books in the binary file.

        Parameters:
            books: List of Book objects to be saved in the binary file.
        """
        with open(self.file_path, 'wb') as file:
            for book in books:
                pickle.dump(book, file)