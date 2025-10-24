from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def web_view(request):
    return render(request, "website/web_index.html")


def contact_view(request):
    return render(request, "website/contact.html")


def address_view(request):
    return render(request, "website/address.html")


def host_view(request):
    return render(request, "website/host.html")


def test_view(request):
    return render(request, 'website/test.html', {"name": "arvin", "age": 16})
