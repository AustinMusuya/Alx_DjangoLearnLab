from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework import generics, viewsets

# authentication & Permisions api views
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

# view to serialize data from Book Model


class BookList(generics.ListAPIView,APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        return Response({'message': 'Hello authenticated user'})


# viewset to perform CRUD operations

class BookViewSet(viewsets.ModelViewSet, APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get(self, request):
        return Response({'message': 'Hello authenticated user'})
