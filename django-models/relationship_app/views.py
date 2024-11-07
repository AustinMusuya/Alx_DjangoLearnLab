from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView, ListView

# Create your views here.


def book_list(request):
    # list of all book instances
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class BookDetailView(ListView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
