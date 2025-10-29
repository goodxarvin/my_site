from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from contact.models import Submitted


def web_view(request):
    return render(request, "website/web_index.html")


def contact_view(request):
    return render(request, "website/contact.html")


def address_view(request):
    return render(request, "website/address.html")


def host_view(request):
    return render(request, "website/host.html")


def test_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

    contact = Submitted()
    contact.name = name
    contact.email = email
    contact.subject = subject
    contact.message = message
    contact.save()

    if request.method == "GET":
        print("get")
    return render(request, 'website/test.html', {"name": "arvin", "age": 16})
