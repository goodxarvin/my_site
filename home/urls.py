from django.urls import path, include
from home.views import home_view, home_about_view

urlpatterns = [
    path("", home_view),
    path("about", home_about_view)
]
