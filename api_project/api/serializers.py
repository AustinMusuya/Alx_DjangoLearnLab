from rest_framework import serializers
from .models import Book

# simple serializer for book model


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
