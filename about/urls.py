from django.contrib import admin
from django.urls import path, include
from about.views import main_about_page

app_name = "about"

urlpatterns = [
    path("", main_about_page, name="about"),
]
