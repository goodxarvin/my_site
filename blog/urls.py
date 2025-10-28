from django.urls import path, include
from blog.views import single_view, home_view, category_view

app_name = "blog"

urlpatterns = [
    path("", home_view, name="home"),
    path("post-<slug:slug>-<int:post_id>", single_view, name="single"),
    path("categories/<str:category_type>",
         category_view, name="categories")
    # path("name/<str:name>/email/<str:email>/year/<int:year>", test_view, name="test"),
    # path("post-<slug:slug>-<int:post_id>", post_view, name="details")
]
