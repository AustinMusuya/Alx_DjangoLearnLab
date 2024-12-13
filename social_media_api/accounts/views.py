from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import serializers, viewsets, views
from django.contrib.auth import get_user_model, authenticate
from .serializers import UserSerializer, LoginSerializer

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
        # Check if user already exists
        if User.objects.filter(username=request.data.get('username')).exists():
            return Response({"message": "A user with that username already exists."},
                            status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=request.data.get('email')).exists():
            return Response({"message": "A user with that email already exists."},
                            status=status.HTTP_400_BAD_REQUEST)
        
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
    serializer_class = LoginSerializer

    def get(self, request):
        return Response(
            {
                "message": "Use POST request and enter username and password to login user"
            },
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
                )

            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response(
                    {
                        'message': 'Login succesful.',
                        'token': token.key
                    },
                    status=status.HTTP_200_OK
                )

        return Response({'Message': 'Invalid Username and Password'}, status=status.HTTP_401_UNAUTHORIZED)


class ProfileView(TemplateView, LoginRequiredMixin):
    template_name = 'accounts/profile.html'


class FollowUser(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = User.objects.get(id=user_id)
            if request.user != user_to_follow:
                request.user.following.add(user_to_follow)
                return Response({'message': 'User followed successfully!'}, status=status.HTTP_200_OK)
            return Response({'error': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        
class UnfollowUser(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = User.objects.get(id=user_id)
            if request.user != user_to_unfollow:
                request.user.following.remove(user_to_unfollow)
                return Response({'message': 'User unfollowed successfully!'}, status=status.HTTP_200_OK)
            return Response({'error': 'You cannot unfollow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
