from django.urls import path
from website.views import web_view, contact_view, address_view, host_view

urlpatterns = [
    path("", web_view),
    path("contact", contact_view),
    path("address", address_view),
    path("host", host_view)
]
