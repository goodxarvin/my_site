from django.urls import path
from user_management.views import CustomLoginView

app_name = "user"

urlpatterns = [
    path("accounts/login/", CustomLoginView.as_view(), name="account_login"),
]
