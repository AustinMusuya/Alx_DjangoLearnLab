from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm, UpdateForm, PostForm
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

# Create your views here.


class Home(TemplateView):
    template_name = 'blog/base.html'

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'
    

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("/")
    template_name = 'blog/post_confrim_delete.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class Register(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

@login_required(login_url='/login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = PostForm()
        return render(request, 'blog/create-post.html', {'form': form})

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

