from django.shortcuts import render
from blog.models import Post


def single_view(request):
    return render(request, "travelista/blog/blog-single.html")


def home_view(request):
    published_posts = Post.objects.filter(status=1)
    published_posts_dict = {"published_posts": published_posts}
    return render(request, "travelista/blog/blog-home.html", published_posts_dict)


def test_view(request):
    return render(request, "travelista/blog/test.html")
