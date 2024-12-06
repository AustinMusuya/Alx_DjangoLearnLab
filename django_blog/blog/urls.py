from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    path('accounts/profile', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('update/', views.user_update, name='update'),
    path('posts/', views.Home.as_view(), name='posts'),
    path('logout/', views.Home.as_view(), name='logout'),
    # path urls for CRUD actions on posts
    path('post/create/', views.PostCreateView.as_view(), name='create-post'),
    path('post/list-view/', views.PostListView.as_view(), name='list-post'),
    path('post/<int:pk>/detail/', views.PostDetailView.as_view(), name='detail-post'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='update-post'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete-post'),

]
