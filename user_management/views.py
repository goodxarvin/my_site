from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def login_view(request):
    if request.method == "POST" and not request.user.is_authenticated:
        form = AuthenticationForm(
            request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("/")

            else:
                messages.add_message(request, messages.ERROR,
                                     "wrong username or password")
    else:
        return redirect("/")

    context = {"request": request}
    return render(request, "travelista/user_management/login.html", context)


# def logout_view(request):
#     return render(request, "travelista/user_managment/logout.html")


def signup_view(request):
    return render(request, "travelista/user_management/signup.html")
