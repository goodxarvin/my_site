from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.db.models import F
from django.utils import timezone


def single_view(request, slug, post_id):
    post = get_object_or_404(Post, pk=post_id, status=1)
    # posts = Post.objects.filter(status=1)
    # post = get_object_or_404(posts, pk=post_id) ==> second way for the top code
    paragraph = post.content.split("\n")
    context = {"post": post, "paragraph": paragraph}
    return render(request, "travelista/blog/blog-single.html", context)


def home_view(request):
    Post.objects.filter(
        published_date__lte=timezone.now()).update(status=1)
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
