from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.db.models import F, Max
from django.utils import timezone


def get_prev_next(post_id: int):
    prev_post = None
    next_post = None
    max_id = Post.objects.aggregate(Max("id"))["id__max"]
    for prev in range(post_id-1, 0, -1):
        if Post.objects.filter(id=prev, status=1).exists():
            prev_post = get_object_or_404(Post, pk=prev, status=1)
            break
    for the_next in range(post_id+1, max_id+1):
        if Post.objects.filter(id=the_next, status=1).exists():
            next_post = get_object_or_404(Post, pk=the_next, status=1)
            break

    return prev_post, next_post


def single_view(request, slug, post_id):
    post = get_object_or_404(Post, pk=post_id, status=1)
    prev_p, next_p = get_prev_next(post_id)
    Post.objects.filter(id=post_id, slug=slug).update(
        counted_views=F("counted_views") + 1)
    # posts = Post.objects.filter(status=1)
    # post = get_object_or_404(posts, pk=post_id) ==> second way for the top code

    paragraph = post.content.split("\n")
    context = {"post": post, "paragraph": paragraph,
               "next": next_p, "prev": prev_p}
    return render(request, "travelista/blog/blog-single.html", context)


def home_view(request, **kwargs):
    Post.objects.filter(
        published_date__lte=timezone.now()).update(status=1)
    published_posts = Post.objects.filter(status=1)
    if kwargs.get("category_type"):
        published_posts = published_posts.filter(
            category__category_type=kwargs["category_type"])
    if kwargs.get("author_username"):
        published_posts = published_posts.filter(
            author__username=kwargs["author_username"])
    published_posts_dict = {"published_posts": published_posts}
    return render(request, "travelista/blog/blog-home.html", published_posts_dict)


# def test_view(request, name, email, year):
#     name_dict = {"name": name, "email": email, "year": year}
#     return render(request, "travelista/blog/test.html", name_dict)


# def test(request):
#     return render(request, "travelista/blog/test.html")


# def post_view(request, slug, post_id):
#     # post = Post.objects.get(id=pid)
#     post = get_object_or_404(Post, pk=post_id)
#     Post.objects.filter(id=post_id, slug=slug).update(
#         counted_views=F("counted_views") + 1)
#     post.refresh_from_db()
#     context = {"post": post}
#     return render(request, "travelista/blog/id.html", context)

# def category_view(request, category_type):
#     category_posts = Post.objects.filter(
#         status=1, category__category_type=category_type)
#     context = {"published_posts": category_posts,
#                "category_type": category_type}
#     return render(request, "travelista/blog/blog-home.html", context)
