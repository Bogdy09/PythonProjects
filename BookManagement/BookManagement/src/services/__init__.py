# Services class
from src.domain import Book


class Services:
    def __init__(self, repository, File_repository, Binary_repository):
        self.repository = repository
        self.fileRepository=File_repository
        self.BinaryRepository=Binary_repository

    def save_history(self, operation, data_before, data_after):
        """
               Saves the history of operations performed on the repository.

               Parameters:
                   operation (str): Type of operation performed.
                   data_before: Data before the operation.
                   data_after: Data after the operation.
        """
        self.history.append((operation, data_before, data_after))

    def undo_last_operation(self):
        self.repository.undo_last_operation()
        self.fileRepository.update_file_from_repository()

    def get_current_state(self):
        """
                Retrieves the current state of the repository.

                Returns:
                    Current state data.
        """
        # Implement a method to retrieve the current state of your repository
        return self.repository.get_state()

    def is_unique_isbn(self, isbn):
        """
                Checks if the ISBN provided for a book is unique within the repository.

                Parameters:
                    isbn: ISBN to be checked for uniqueness.

                Returns:
                    True if the ISBN is unique, False otherwise.
        """
        existing_isbns = [book.isbn for book in self.repository.get_books()]
        return isbn not in existing_isbns


    def add_book(self, isbn, author, title):
        """
               Adds a new book to the repository.

               Parameters:
                   isbn: ISBN of the new book.
                   author: Author of the new book.
                   title: Title of the new book.
        """

        if not isbn or not author or not title:
            raise ValueError("Invalid input")
        if not self.is_unique_isbn(isbn):
            raise ValueError("ISBN is not unique")
        if not isinstance(author, str):
            raise ValueError("Author must be a string")
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        self.repository.save_state()  # Save the current state before adding a book
        book = Book(isbn, author, title)
        self.repository.add_book(book)
        self.fileRepository.add_book(book)
        updated_books = self.repository.get_books()

        # Update the binary file with the latest book list
        self.BinaryRepository.update_file(updated_books)
        self.BinaryRepository.save_state(self.repository.get_books())


    def filter_books(self, word):
        all_books = self.repository.get_books()
        first_words = [book.title.split()[0] for book in all_books]

        if word not in first_words:
            raise ValueError(f"'{word}' is not valid")

        self.repository.save_state()  # Save the current state before filtering

        # Filter books in memory
        filtered_books = [book for book in all_books if not book.title.startswith(word)]

        # Update repository books by excluding filtered books
        self.repository.books = filtered_books

        # Update the file with the filtered books
        self.fileRepository.filter_books_and_update_file(word)
        self.repository.books = filtered_books

        # Update binary file repository with the filtered books
        self.BinaryRepository.update_file(filtered_books)
        self.BinaryRepository.save_state(self.repository.get_books())

    def get_books(self):
        return self.repository.get_books()

    def load(self):
        """
               Loads data into the repository from a text file repository.
        """
        self.repository.books=self.fileRepository.get_books()

    def load1(self):
        """
               Loads data into the repository from a binary file repository.
        """
        self.repository.books = self.BinaryRepository.get_books()

    def undo_last_operation(self):
        self.repository.undo_last_operation()
        self.BinaryRepository.save_state(self.repository.get_books())