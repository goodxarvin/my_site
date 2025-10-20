from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def contact_view(request):
    return HttpResponse("<b><h1>contact page<h1><b>")


def address_view(request):
    return HttpResponse("<b><h1>address page<h1><b>")


def host_view(request):
    return HttpResponse("<b><h1>host page<h1><b>")
