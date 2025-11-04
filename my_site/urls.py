"""
URL configuration for my_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from home.sitemaps import HomeStaticViewSitemap
from contact.sitemaps import ContactStaticViewSitemap
from about.sitemaps import AboutStaticViewSitemap
from blog.sitemaps import BlogSitemap
from debug_toolbar.toolbar import debug_toolbar_urls

sitemaps = {"home": HomeStaticViewSitemap,
            "contact": ContactStaticViewSitemap,
            "about": AboutStaticViewSitemap,
            "blog": BlogSitemap}


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("website/", include("website.urls"), name="web"),
    path("about/", include("about.urls")),
    path("contact/", include("contact.urls")),
    path("elements/", include("elements.urls")),
    path("blog/", include("blog.urls")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps},
         name="django.contrib.sitemaps.views.sitemap"),
    path("robots.txt", include("robots.urls")),
    path('summernote/', include('django_summernote.urls')),
    path("user-management/", include("user_management.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += debug_toolbar_urls()
urlpatterns += [path('captcha/', include('captcha.urls')),]
