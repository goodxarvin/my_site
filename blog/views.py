from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.db.models import F, Max, Q
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    context = {"post": post, "next": next_p, "prev": prev_p}
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

    if kwargs.get("tag_name"):
        published_posts = published_posts.filter(
            tag__name__in=[kwargs["tag_name"]])

    paged_published_posts = Paginator(published_posts, 3)
    try:
        page_number = request.GET.get("page-num")
        paged_published_posts = paged_published_posts.get_page(page_number)

    except PageNotAnInteger:
        paged_published_posts = paged_published_posts.get_page(1)

    except EmptyPage:
        paged_published_posts = paged_published_posts.get_page(1)

    published_posts_dict = {"paged_published_posts": paged_published_posts}
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

def search_view(request):
    posts = Post.objects.filter(status=1)
    if request.method == "GET":
        if search_word := request.GET.get("search-element"):
            posts = posts.filter(
                Q(content__contains=search_word) | Q(title__contains=search_word))
    paged_published_posts = Paginator(posts, 3)
    try:
        page_num = request.GET.get("page-num")
        paged_published_posts = paged_published_posts.get_page(page_num)
    except PageNotAnInteger:
        paged_published_posts = paged_published_posts.get_page(1)
    except EmptyPage:
        paged_published_posts = paged_published_posts.get_page(1)

    qs = request.GET.copy()
    if "page-num" in qs:
        qs.pop("page-num")
    querystring = qs.urlencode()

    context = {"paged_published_posts": paged_published_posts,
               "querystring": querystring}
    return render(request, "travelista/blog/blog-home.html", context)
