from django.contrib import admin
from django.urls import path, include
from contact.views import contact_main_page

app_name = "contact"


urlpatterns = [
    path("", contact_main_page, name="contact"),
]
