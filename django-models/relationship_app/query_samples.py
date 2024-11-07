"""
Query all books by a specific author.
List all books in a library.
Retrieve the librarian for a library.

"""
from .models import Author, Book, Library, Librarian

# Query all books by a specific author.

books_by_author = Book.objects.filter(author__name="J.K. Rowling")
