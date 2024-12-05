from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('profile/', views.Home.as_view(), name='profile'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('posts/', views.Home.as_view(), name='posts'),
    path('logout/', views.Home.as_view(), name='logout'),
]
