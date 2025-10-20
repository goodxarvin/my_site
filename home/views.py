from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return HttpResponse("<b><h1>you're in the home page :)<h1><b>")


def home_info_view(request):
    return HttpResponse("<b><h1>home info<h1><b>")
