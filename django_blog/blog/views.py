from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserUpdateForm, ProfileForm
from .models import Profile
from django.contrib import messages

@login_required
def profile(request):
    Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, "Profile updated.")
            return redirect("blog:profile")
        messages.error(request, "Please fix the errors below.")
    else:
        uform = UserUpdateForm(instance=request.user)
        pform = ProfileForm(instance=request.user.profile)

    return render(request, "blog/auth/profile.html", {"uform": uform, "pform": pform})
