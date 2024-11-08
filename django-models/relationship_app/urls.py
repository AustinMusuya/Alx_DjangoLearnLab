from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth import views

urlpatterns = [
    path('', view=list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
