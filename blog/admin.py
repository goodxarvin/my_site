from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "published_date"
    empty_value_display = "--empty--"
    # fields = ("title", "content", "status")
    # exclude = ("counted_views", "published_date")
    list_display = ("id", "title", "status", "created_time", "author")
    list_filter = ("status", "created_time", "author")
    # ordering = ["-created_time"]
    search_fields = ["title", 'content']


# admin.site.register(Post, PostAdmin)
