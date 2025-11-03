from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post


class LatestBlogs(Feed):
    title = "best latest blogs"
    link = "/rss/feed"
    description = "update latest blogs"

    def items(self):
        return Post.objects.filter(status=1)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]
