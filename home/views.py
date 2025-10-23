from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return render(request, "travelista_main_page/index.html")


def home_about_view(request):
    return render(request, "travelista_main_page/about.html")
