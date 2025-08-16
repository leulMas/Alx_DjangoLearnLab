from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from .forms import RegisterForm, UserUpdateForm, ProfileForm
from .models import Profile

class BlogLoginView(LoginView):
    template_name = "blog/auth/login.html"

class BlogLogoutView(LogoutView):
    pass  # LOGOUT_REDIRECT_URL handles redirect

def register(request):
    if request.user.is_authenticated:
        return redirect("blog:profile")
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            Profile.objects.get_or_create(user=user)
            messages.success(request, "Account created. You can log in now.")
            return redirect("blog:login")
        messages.error(request, "Please correct the errors below.")
    return render(request, "blog/auth/register.html", {"form": form})

@login_required
def profile(request):
    Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if uform.is_valid() and pform.is_valid():
            uform.save(); pform.save()
            messages.success(request, "Profile updated.")
            return redirect("blog:profile")
        messages.error(request, "Please fix the errors below.")
    else:
        uform = UserUpdateForm(instance=request.user)
        pform = ProfileForm(instance=request.user.profile)
    return render(request, "blog/auth/profile.html", {"uform": uform, "pform": pform})
