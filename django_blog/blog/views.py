from django.shortcuts import render
from .forms import RegisterForm
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

# Create your views here.


class Home(TemplateView):
    template_name = 'blog/base.html'

class Register(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
