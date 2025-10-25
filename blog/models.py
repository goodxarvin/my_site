from django.db import models


class Post(models.Model):
    # image
    # author
    # tag
    # category
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField(default=False)
    counted_views = models.IntegerField(default=0)
    published_date = models.DateTimeField(null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


# 