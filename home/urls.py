from django.urls import path, include
from home.views import home_view

urlpatterns = [
    path("", home_view, name="index")
]
