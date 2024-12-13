from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('api-register/', views.RegistrationAPIView.as_view(), name='api-register'),
    path('api-login/', views.LoginAPIView.as_view(), name='api-login'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('api-token-auth/', ObtainAuthToken.as_view(), name='api-token-auth'),
    path('follow/<int:user_id>/', views.FollowUser.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', views.UnfollowUser.as_view(), name='unfollow-user'),

    # viewset for router urls
    path('api/', include(router.urls))
]
