from django.contrib import admin
from django.urls import path, include
from elements.views import elements_main_page

app_name = "elements"


urlpatterns = [
    path("", elements_main_page, name="elements"),
]
