from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from main_app.app_forms import LoginForm, UserForm
from main_app.models import Donors


# Create your views here.
@login_required()
def home(request):
    return render(request, "index.html")


@login_required
def about(request):
    return render(request, "about.html")


@login_required
def contact(request):
    return render(request, "contact.html")


def signin(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
        messages.error(request, "Wrong username or password")
        return render(request, "login.html", {"form": form})


@login_required
def profile(request):
    user = Donors.objects.all()
    return render(request, "profile.html", {"user": user})


@login_required
def signout(request):
    logout(request)
    return redirect('signin')


def book(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = UserForm()
    return render(request, "book-appointement.html", {"form": form})
