from django.urls import path
from user_management.views import login_view, signup_view

app_name = "user"

urlpatterns = [
    path("login", login_view, name="login"),
    # path("logout", logout_view, name="logout"),
    path("signup", signup_view, name="signup"),


]
