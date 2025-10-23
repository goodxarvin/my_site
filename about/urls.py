from django.contrib import admin
from django.urls import path, include
from about.views import main_about_page

urlpatterns = [
    path("", main_about_page),
]
