from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework import generics, viewsets

# Create your views here.

# view to serialize data from Book Model


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# viewset to perform CRUD operations

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
