from django.urls import path, include
from blog.views import single_view, home_view, search_view
from blog.feeds import LatestBlogs

app_name = "blog"

urlpatterns = [
    path("", home_view, name="home"),
    path("post-<slug:slug>-<int:post_id>", single_view, name="single"),
    path("categories/<str:category_type>", home_view, name="categories"),
    path("tags/<str:tag_name>", home_view, name="tags"),
    path("categories/", home_view),
    path("writer/<str:author_username>", home_view, name="author"),
    path("rss/feed/", LatestBlogs()),
    path("search/", search_view, name="search")
    # path("name/<str:name>/email/<str:email>/year/<int:year>", test_view, name="test"),
    # path("post-<slug:slug>-<int:post_id>", post_view, name="details")
]
