from django.urls import path, include
from home.views import home_view, about_view, contact_view

app_name = "home"

urlpatterns = [
    path("", home_view, name="index"),
    path("about/", about_view, name="about"),
    path("contact/", contact_view, name="contact")
]
