from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm, UpdateForm
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

# Create your views here.


class Home(TemplateView):
    template_name = 'blog/base.html'

class Register(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

@login_required(login_url='/login')
def user_update(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=request.user)  # instantiate the form object
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UpdateForm(instance=request.user) # instantiate the form object
    return render(request, 'registration/update.html', {'form': form})

