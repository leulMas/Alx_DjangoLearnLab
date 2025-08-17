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
    
