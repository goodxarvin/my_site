from django.urls import path
from user_management.views import CustomLoginView, CustomSignUpview, profile_view

app_name = "user"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="account_login"),
    path("signup/", CustomSignUpview.as_view(), name="account_signup"),
    path("profile/", profile_view, name="account_profile"),
]
