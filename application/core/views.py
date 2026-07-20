from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from .forms import UserLoginForm

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

# Simple log in function
def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

        username = data["username"].lower()
        password = data["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "You have succesfully logged in")
        else:
            messages.add_message(request, messages.ERROR, "Invalid log in credentials, please try again")

        return redirect("core:home")
    else:
        form = UserLoginForm()
        return render(request, "core/login.html", {"form":form})

def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "You have successfully logged out")
    return redirect("core:home")