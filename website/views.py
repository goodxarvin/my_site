from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from contact.models import Submitted
from website.forms import SubmitForm


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
        contact = SubmitForm(request.POST)
        if contact.is_valid():
            contact.save()

            return HttpResponse(f"successful")
        else:
            return HttpResponse("invalid")

    contact = SubmitForm()
    return render(request, 'website/test.html', {"forms": contact})
