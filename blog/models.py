from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class Category(models.Model):
    category_type = models.CharField(max_length=100)

    def __str__(self):
        return self.category_type


class Post(models.Model):
    image = models.ImageField(upload_to="blog/", default="blog/default.jpg")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tag = TaggableManager()
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField(default=False)
    counted_views = models.IntegerField(default=0)
    published_date = models.DateTimeField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

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

    def get_absolute_url(self):
        return reverse("blog:single", kwargs={"slug": self.slug, "post_id": self.id})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    email = models.EmailField()
    image = models.ImageField(upload_to="blog/", default="blog/dog.jpg")
    comment_content = models.TextField()
    approved = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
