from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ProfileUpdate, CustomUser
from .forms import RegisterForm, ProfileUpdateForm

def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login/')
def base(request):
    return render(request, 'base.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Invalid credentials")
    return render(request, "login.html")

@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def user_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    profile, created = ProfileUpdate.objects.get_or_create(user=user)
    return render(request, 'user_profile.html', {
        'profile_user': user,
        'profile': profile,
    })

@login_required
def profile_update(request):
    # Get or create profile for the current user
    profile, created = ProfileUpdate.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("user_profile", username=request.user.username)
    else:
        form = ProfileUpdateForm(instance=profile)
    
    return render(request, "profile_update.html", {"form": form})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})