from django.contrib import admin
from django.urls import path, include
from contact.views import contact_main_page

urlpatterns = [
    path("", contact_main_page),
]
