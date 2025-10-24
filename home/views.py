from django.shortcuts import render
from django.http import HttpResponse

app_name = "home"


def home_view(request):
    return render(request, "resume/index.html")
