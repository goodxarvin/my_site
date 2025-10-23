from django.shortcuts import render


def contact_main_page(request):
    return render(request, "travelista/contact.html")
