from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.ListView.as_view(), name='book-list'),
]