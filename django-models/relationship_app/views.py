from django.shortcuts import render
from .models import Book

# Create your views here.


def book_list(request):
    # list of all book instances
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
