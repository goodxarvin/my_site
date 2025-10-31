from django.contrib import sitemaps
from django.urls import reverse


class ContactStaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["contact:contact"]

    def location(self, item):
        return reverse(item)
