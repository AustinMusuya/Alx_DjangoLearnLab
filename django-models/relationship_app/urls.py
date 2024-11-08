from django.urls import path
from .views import book_list, LibraryDetailView

urlpatterns = [
    path('', view=book_list, name='book_list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail')
]
