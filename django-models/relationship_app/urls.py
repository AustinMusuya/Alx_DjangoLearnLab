from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', view=list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
