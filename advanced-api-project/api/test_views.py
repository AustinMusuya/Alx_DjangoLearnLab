from rest_framework.test import APIRequestFactory
from .views import ListView
from rest_framework import status
from django.test import TestCase

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
