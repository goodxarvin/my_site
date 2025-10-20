from django.urls import path
from website.views import contact_view, address_view, host_view

urlpatterns = [
    path("contact", contact_view),
    path("address", address_view),
    path("host", host_view)
]
