from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from rest_framework import serializers, viewsets
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()

# Create your views here.

# home view
class HomeView(TemplateView):
    template_name = 'accounts/home.html'



class RegistrationView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class ProfileView(TemplateView, LoginRequiredMixin):
    template_name = 'accounts/profile.html'

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
