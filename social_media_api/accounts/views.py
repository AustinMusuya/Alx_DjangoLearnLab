from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers, viewsets, views
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


class RegistrationAPIView(views.APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        return Response(
            {
                "message": "Use POST request and enter email and password to register new user"
            },
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    'message': "new user created successfully",
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                        "token": user.token
                    }
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(views.APIView):
    pass


class ProfileView(TemplateView, LoginRequiredMixin):
    template_name = 'accounts/profile.html'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
