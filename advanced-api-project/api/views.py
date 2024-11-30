from django.shortcuts import render
from rest_framework import generics
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# Create your views here.

"""
Implement a set of generic views for the Book model to handle CRUD operations. This includes:
A ListView for retrieving all books.
A DetailView for retrieving a single book by ID.
A CreateView for adding a new book.
An UpdateView for modifying an existing book.
A DeleteView for removing a book.

"""
# A ListView for retrieving all books.
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# A DetailView for retrieving a single book by ID.
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# A CreateView for adding a new book.
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# An UpdateView for modifying an existing book.
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# A DeleteView for removing a book.
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer