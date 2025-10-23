from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def main_about_page(request):
    return render(request, "travelista/about.html")
