from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegisterForm, UpdateForm, PostForm
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

# Create your views here.


class Home(TemplateView):
    template_name = 'blog/base.html'

# User Sign Up/Register view 
class Register(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')    


# CRUD Views opertions on POSTS by users
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def test_func(self):
        # Allow only the author of the post to delete it
        post = self.get_object()  # Get the current post instance
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        # Allow only the author of the post to delete it
        post = self.get_object()  # Get the current post instance
        return self.request.user == post.author

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        # Set the author to the currently logged-in user
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        # Redirect to the list view after successful creation
        return reverse_lazy('post-list')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
# CRUD Operation Views on Comments

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['post','content']
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        # Set the author to the currently logged-in user
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        # Redirect to the list view after successful creation
        return reverse_lazy('comment-list')
    

class CommentListView(ListView):
    model = Comment
    context_object_name = 'comments'
    template_name = 'blog/post_comments.html'


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'

    def test_func(self):
        # Allow only the author of the comment to delete it
        comment = self.get_object()  # Get the current comment instance
        return self.request.user == comment.author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy("post_list")
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        # Allow only the author of the comment to delete it
        comment = self.get_object()  # Get the current comment instance
        return self.request.user == comment.author



    # Redundant Code 

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
        return render(request, 'blog/post_form.html', {'form': form})

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

