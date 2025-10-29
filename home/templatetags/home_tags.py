from django import template
from blog.models import Post

register = template.Library()


@register.inclusion_tag("travelista/home/add_lastest_tags.html")
def get_lastest_blogs():
    posts = Post.objects.filter(status=1)[:6]
    last_six_posts = {"posts": posts}
    return last_six_posts
