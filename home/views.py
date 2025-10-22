from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return render(request, "index.html")


def home_info_view(request):
    return render(request, "info.html")
