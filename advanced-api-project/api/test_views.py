from rest_framework.test import APIRequestFactory, APITestCase
from .views import ListView
from rest_framework import status
from django.test import TestCase
from .models import Book, Author
from django.urls import reverse

# factory = APIRequestFactory()

# request = factory.get('books/')
# view = ListView.as_view()
# response = view(request)

# print(response.status_code)
# print(response.data)


class BooksListViewTestCase(TestCase):
    def setUp(self):
        """Set up test prerequisites."""
        self.factory = APIRequestFactory()

    def test_books_endpoint_returns_200(self):
        """Test that the books endpoint returns a 200 status."""
        request = self.factory.get('/books/')
        view = ListView.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

class BooksDetailViewTestCase(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(title='Introduction to Java', publication_year="2024-05-05", author=self.author)
        self.valid_url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.invalid_url = reverse('book-detail', kwargs={'pk': 9999})
    
    def test_book_detail_valid_pk(self):
        """Test retrieving a book with a valid primary key."""
        response = self.client.get(self.valid_url)  # Simulate a GET request
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Expect 200 OK
        self.assertEqual(response.data['title'], self.book.title)  # Validate title
        self.assertEqual(response.data['author'], self.author.id)  # Validate author

    def test_book_detail_invalid_pk(self):
        """Test retrieving a book with an invalid primary key."""
        response = self.client.get(self.invalid_url)  # Simulate a GET request
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)  # Expect 404

