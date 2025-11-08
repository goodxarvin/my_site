from django.urls import path
from user_management.views import CustomLoginView, CustomSignUpview, profile_view

app_name = "user"

urlpatterns = [
    path("accounts/login/", CustomLoginView.as_view(), name="account_login"),
    path("accounts/signup/", CustomSignUpview.as_view(), name="account_signup"),
    path("accounts/profile", profile_view, name="account_profile"),
]
