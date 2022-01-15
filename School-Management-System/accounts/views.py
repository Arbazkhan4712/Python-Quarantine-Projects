from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserLoginForm

# Create your views here.
def user_login(request):
    forms = UserLoginForm()
    if request.method == "POST":
        forms = UserLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data["username"]
            password = forms.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid User or Password")
                return redirect("login")

    context = {
        "forms": forms
    }
    return render(request, "accounts/login.html", context)

def user_logout(request):
    logout(request)
    return redirect("login")

