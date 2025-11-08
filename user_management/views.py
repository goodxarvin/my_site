from django.shortcuts import render, redirect
from django import forms
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm  # , UserCreationForm
# from django.contrib import messages
# from user_management.forms import UserForm
from allauth.account.views import LoginView, SignupView
from django.contrib import messages


class CustomLoginView(LoginView):
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f'{error}')
        return super().form_invalid(form)


class CustomSignUpview(SignupView):
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{error}")
        return super().form_invalid(form)


@login_required()
def profile_view(request):
    return render(request, "account/profile.html")


# def login_view(request):
#     if not request.user.is_authenticated:
#         if request.method == "POST":
#             form = AuthenticationForm(
#                 request=request, data=request.POST)
#             if form.is_valid():
#                 username = form.cleaned_data.get("username")
#                 password = form.cleaned_data.get("password")
#                 user = authenticate(
#                     request, username=username, password=password)
#                 login(request, user)
#                 messages.add_message(
#                     request, messages.SUCCESS, f"you logged in successfully as {request.user.username}")
#                 return redirect("/")

#             else:
#                 messages.add_message(request, messages.ERROR,
#                                     "wrong username or password")
#     else:
#         messages.add_message(
#             request, messages.INFO, "you're already logged in please logout to proceed the following task")
#         return redirect("/")

#     return render(request, "travelista/user_management/login.html")


# @login_required()
# def logout_view(request):
#     messages.add_message(request, messages.SUCCESS, "logged out successfully")
#     logout(request)
#     return redirect("/")


# def signup_view(request):
#     if not request.user.is_authenticated:
#         if request.method == "POST":
#             form = UserForm(request.POST)
#             if form.is_valid():
#                 messages.add_message(
#                     request, messages.SUCCESS, "your account created successfully")
#                 form.save()
#                 return redirect("/user-management/login")
#             else:
#                 messages.add_message(
#                     request, messages.ERROR, "your account didn't created")
#     else:
#         messages.add_message(
#             request, messages.INFO, "you're already logged in please logout to proceed the following task")
#         return redirect("/")

#     return render(request, "travelista/user_management/signup.html")
