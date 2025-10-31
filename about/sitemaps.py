from django.contrib import sitemaps
from django.urls import reverse


class AboutStaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["about:about"]

    def location(self, item):
        return reverse(item)
