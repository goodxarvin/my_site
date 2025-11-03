from django.shortcuts import render


def login_view(request):
    return render(request, "travelista/user_management/login.html")


# def logout_view(request):
#     return render(request, "travelista/user_managment/logout.html")


def signup_view(request):
    return render(request, "travelista/user_management/signup.html")
