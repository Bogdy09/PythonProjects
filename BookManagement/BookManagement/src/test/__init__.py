import unittest
from src.services import Services
from src.domain import Book
from src.repository import MemoryRepository, TextFileRepository, BinaryFileRepository


class TestServices(unittest.TestCase):
    def setUp(self):
        self.memory_repo = MemoryRepository()
        self.text_file_repo = TextFileRepository('books.txt', self.memory_repo)
        self.binary_file_repo = BinaryFileRepository('books.pkl')

        # Initialize repositories with necessary data for testing
        # (Adding some test books for example)
        for i in range(5):
            book = Book(f"ISBN{i}", f"Author{i}", f"Title{i}")
            self.text_file_repo.add_book(book)
            self.binary_file_repo.add_book(book)
            self.memory_repo.add_book(book)

        self.services = Services(self.memory_repo, self.text_file_repo, self.binary_file_repo)
    def test_add_book(self):
        # Test adding a book
        self.services.add_book("1234567890", "John Doe", "Test Book")
        books = self.services.get_books()
        self.assertEqual(len(books), 6)
        # Add more assertions as needed

    def test_undo_last_operation(self):
        # Test undoing the last operation
        self.services.add_book("0987654321", "Jane Smith", "Another Book")
        self.services.undo_last_operation()
        books = self.services.get_books()
        self.assertEqual(len(books), 5)
        # Add more assertions as needed

    def test_filter_books(self):
        # Test filtering books
        self.services.add_book("1111111111", "Author1", "Title1")
        self.services.add_book("2222222222", "Author2", "Title2")
        self.services.add_book("3333333333", "Author3", "Title3")

        self.services.filter_books("Title1")
        books = self.services.get_books()
        # Check if filtered books are correct
        self.assertEqual(len(books), 6)
        # Add more assertions as needed

    # Add more test cases for other functions

if __name__ == '__main__':
    unittest.main()