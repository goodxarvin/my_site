from django.urls import path, include
from home.views import home_view, home_info_view

urlpatterns = [
    path("", home_view),
    path("info", home_info_view)
]
