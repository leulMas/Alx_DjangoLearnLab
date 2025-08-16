# blog/views.py
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from .forms import RegisterForm, UserUpdateForm, ProfileForm
from .models import Profile

# Define BlogLoginView, BlogLogoutView, register(), profile() here
