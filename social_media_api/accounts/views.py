from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# home view
class HomeView(TemplateView):
    template_name = 'accounts/home.html'
