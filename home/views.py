from django.shortcuts import render
from django.http import HttpResponse


my_info = {"name": "Arvin", "last_name": "Behbahani",
           "WF": "django", "phone": "(+98) 933-881-3757",
           "loc": "Iran, Tehran", "email": "arvinbehbahani@gmail.com"}


def home_view(request):

    return render(request, "resume/index.html", my_info)


def about_view(request):
    return render(request, "resume/about.html", my_info)


def contact_view(request):
    return render(request, "resume/contact.html", my_info)
