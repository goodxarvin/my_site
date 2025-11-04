from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(
                request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(
                    request, username=username, password=password)
                login(request, user)
                messages.add_message(
                    request, messages.SUCCESS, f"you logged in successfully as {request.user.username}")
                return redirect("/")

            else:
                messages.add_message(request, messages.ERROR,
                                     "wrong username or password")
    else:
        return redirect("/")

    context = {"request": request}
    return render(request, "travelista/user_management/login.html", context)


@login_required()
def logout_view(request):
    logout(request)
    return redirect("/")


def signup_view(request):
    return render(request, "travelista/user_management/signup.html")
