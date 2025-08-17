# blog/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.shortcuts import render
from .models import Comment




def home_view(request):
   return render(request, "blog/home.html")
   
# Registration view
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("profile")
        else:
            messages.error(request, "Registration failed. Please check the errors.")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome {user.username}!")
            return redirect("profile")
        else:
            messages.error(request, "Login failed. Check username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})

# Logout view
def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login")

# Profile view
@login_required
def profile_view(request):
    if request.method == "POST":
        user = request.user
        email = request.POST.get("email")
        if email:
            user.email = email
            user.save()
            messages.success(request, "Profile updated successfully.")
    return render(request, "blog/profile.html")
    
    
def post_search(request):
    query = request.GET.get('q', '')  # get search query from URL ?q=...
    results = Post.objects.none()     # default empty queryset

    if query:
        results = Post.objects.filter(
            title__icontains=query
        ) | Post.objects.filter(
            content__icontains=query
        ) | Post.objects.filter(
            tags__name__icontains=query
        ).distinct()

    return render(request, 'blog/post_search.html', {'results': results, 'query': query})
    
class CommentCreateView(CreateView):
    model = Comment
    fields = ['content']
    template_name = 'comments/comment_form.html'
    success_url = '/comments/'
    
class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'comments/comment_form.html'
    success_url = '/comments/'

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comments/comment_confirm_delete.html'
    success_url = '/comments/'
