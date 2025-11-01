from django import template
from blog.models import Post, Category
register = template.Library()


@register.simple_tag(name="adding")
def add(num1=100, num2=10):
    return num1 + num2


@register.simple_tag(name="post_amount")
def post_count():
    return Post.objects.filter(status=1).count()


@register.simple_tag(name="posts")
def post_queries():
    return Post.objects.filter(status=1)


@register.filter
def summerize(value: str, max_length=10):
    return value[:max_length].capitalize() + "..."


@register.inclusion_tag("travelista/blog/latest_posts.html")
def latest_posts(arg=3):
    posts = Post.objects.filter(status=1).order_by("-created_time")[:arg]
    return {"posts": posts}


@register.inclusion_tag("travelista/blog/post_categories.html")
def get_categories():
    categories_dict = {}
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    for category in categories:
        categories_dict[category.category_type] = posts.filter(
            category=category).count()

    return {"categories": categories_dict}


