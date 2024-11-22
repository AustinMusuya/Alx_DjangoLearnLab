from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter() # Create an Instance of DefaultRouter Class
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'), # Maps to the BookList view

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
    
    # path to obtain auth token
    path('api-token-auth', obtain_auth_token),
]
