from rest_framework.serializers import ModelSerializer
from .models import Book

# simple serializer for book model


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
