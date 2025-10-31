from django.contrib import admin
from home.models import NewsLetter


@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ["email"]
