from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ExampleForm
# Create your views here.


# Home Page
class HomeView(TemplateView):
    template_name = 'home.html'
