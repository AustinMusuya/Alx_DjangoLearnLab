"""
Query all books by a specific author.
List all books in a library.
Retrieve the librarian for a library.

"""
from .models import Author, Book, Library, Librarian

# Query all books by a specific author.

books_by_author = Book.objects.filter(author__name="J.K. Rowling")


# List all books in a library.
library_name = "National Library"
library = Library.objects.get(name=library_name)

all_books_in_library = library.books.all()

# Retrieve the librarian for a library.

librarian = Librarian.objects.filter(library__name="National Library")
