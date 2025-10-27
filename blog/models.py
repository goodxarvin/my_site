from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Post(models.Model):
    image = models.ImageField(upload_to="blog/", default="blog/default.jpg")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # tag
    # category
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField(default=False)
    counted_views = models.IntegerField(default=0)
    published_date = models.DateTimeField(null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_time"]
        # verbose_name = "پست"
        # verbose_name_plural = "پست ها 🗿👍"

    def __str__(self):
        return f"{self.id}, {self.title}"
