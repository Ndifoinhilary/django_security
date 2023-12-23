from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from authentication.forms import CreateUserForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "index.html")


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("two_factor:login")
    context = {"form": form}
    return render(request, "register.html", context)


@login_required(login_url="two_factor:login")
def dashboard(request):
    return render(request, "dashboard.html")


def user_logout(request):
    auth.logout(request)
    return redirect("home")


def account_locked(request):
    return render(request, "account.html")
