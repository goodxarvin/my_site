from django.urls import path, include
from blog.views import single_view, home_view, test_view

app_name = "blog"

urlpatterns = [
    path("", home_view, name="home"),
    path("single/", single_view, name="single"),
    path("test/", test_view, name="test")
]
