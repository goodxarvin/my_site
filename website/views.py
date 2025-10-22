from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def web_view(request):
    return render(request, "web_index.html")


def contact_view(request):
    return render(request, "contact.html")


def address_view(request):
    return render(request, "address.html")


def host_view(request):
    return render(request, "host.html")
