# UI class
from src.domain import Book
from src.repository import BinaryFileRepository, TextFileRepository, MemoryRepository
from src.services import Services


class UI:
    def __init__(self, services):
        self.services = services

    def display_books(self):
        books = self.services.get_books()
        if not books:
            print("No books available.")
        else:
            print("List of Books:")
            for book in books:
                print(book)

    def add_book(self):
        print("Enter book details:")
        isbn = input("ISBN: ")
        author = input("Author: ")
        title = input("Title: ")
        try:
            self.services.add_book(isbn, author, title)
            print("Book added successfully.")
        except ValueError as ve:
            print("There was an error")
            print(ve)

    def filter_books(self):
        word = input("Enter word to filter titles: ")
        try:
            self.services.filter_books(word)
            print(f"Books with titles starting with '{word}' have been removed.")
        except ValueError as ve:
            print("There was an error")
            print(ve)

    def undo_last_operation(self):
        self.services.undo_last_operation()
        print("Last operation undone.")

# Main function
def main():
    # Initialize repositories and services
    memory_repo = MemoryRepository()
    text_file_repo = TextFileRepository('books.txt', memory_repo)

    binary_file_repo = BinaryFileRepository('books.pkl')  # Initialize BinaryFileRepository with file path only

    # Adding 10 programmatically generated entries at startup
    for i in range(10):
        book = Book(f"ISBN{i}", f"Author{i}", f"Title {i}")
        text_file_repo.add_book(book)
        binary_file_repo.add_book(book)
        memory_repo.add_book(book)
    services = Services(memory_repo, text_file_repo, binary_file_repo)  # Change this to switch repositories
    ui = UI(services)

    while True:
        print("\nMenu:")
        print("1. Display Books")
        print("2. Add a Book")
        print("3. Filter Books by Title")
        print("4. Undo Last Operation")
        print("5. Use text file")
        print("6. Use binary file")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            ui.display_books()
        elif choice == '2':
            ui.add_book()
        elif choice == '3':
            ui.filter_books()
        elif choice == '4':
            ui.undo_last_operation()
        elif choice == '5':
            ui.services.load()
        elif choice == '6':
            ui.services.load1()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()