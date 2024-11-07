from django.urls import path
from .views import book_list, BookDetailView

urlpatterns = [
    path('', view=book_list, name='book_list'),
    path('booklistview', BookDetailView.as_view(), name='booklistview')
]
