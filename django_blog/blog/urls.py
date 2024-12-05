from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('update/', views.user_update, name='update'),
    path('posts/', views.Home.as_view(), name='posts'),
    path('logout/', views.Home.as_view(), name='logout'),
]
