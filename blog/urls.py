from django.urls import path, include
from blog.views import single_view, home_view, test_view, post_view

app_name = "blog"

urlpatterns = [
    path("", home_view, name="home"),
    path("single/", single_view, name="single"),
    path("name/<str:name>/email/<str:email>/year/<int:year>", test_view, name="test"),
    path("post-<int:post_id>-<str:title>", post_view, name="details")
]
