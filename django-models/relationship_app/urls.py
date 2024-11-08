from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('', view=list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail')
]
