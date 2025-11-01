from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Post, Category


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = "published_date"
    empty_value_display = "--empty--"
    # fields = ("title", "content", "status")
    # exclude = ("counted_views", "published_date")
    list_display = ("id", "title", "status", "created_time", "author")
    list_filter = ("status", "created_time", "author")
    # ordering = ["-created_time"]
    search_fields = ["title", 'content']
    summernote_fields = ('content',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_type"]

# admin.site.register(Post, PostAdmin)
