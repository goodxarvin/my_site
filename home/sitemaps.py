from django.contrib import sitemaps
from django.urls import reverse


class HomeStaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["home:index"]

    def location(self, item):
        return reverse(item)
