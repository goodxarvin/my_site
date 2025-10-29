from django.urls import path
from website.views import web_view, contact_view, address_view, host_view, test_view


app_name = "website"
urlpatterns = [
    path("", web_view),
    path("contact", contact_view),
    path("address", address_view),
    path("host", host_view),
    path("test", test_view, name="test")
]
