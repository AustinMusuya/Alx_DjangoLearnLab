from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('profile/', views.Home.as_view(), name='profile'),
    path('login/', views.Home.as_view(), name='login'),
    path('register/', views.Home.as_view(), name='register'),
    path('posts/', views.Home.as_view(), name='posts'),
    path('logout/', views.Home.as_view(), name='logout'),
]
