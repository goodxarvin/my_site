from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.db.models import F


def single_view(request):
    return render(request, "travelista/blog/blog-single.html")


def home_view(request):
    published_posts = Post.objects.filter(status=1)
    published_posts_dict = {"published_posts": published_posts}
    return render(request, "travelista/blog/blog-home.html", published_posts_dict)


def test_view(request, name, email, year):
    name_dict = {"name": name, "email": email, "year": year}
    return render(request, "travelista/blog/test.html", name_dict)


def post_view(request, slug, post_id):
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post, pk=post_id)
    Post.objects.filter(id=post_id, slug=slug).update(
        counted_views=F("counted_views") + 1)
    post.refresh_from_db()
    context = {"post": post}
    return render(request, "travelista/blog/id.html", context)
