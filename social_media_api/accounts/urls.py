from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users',UserViewSet)

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

    # viewset for router urls
    path('api/', include(router.urls))
]
