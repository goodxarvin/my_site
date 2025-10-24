from django.shortcuts import render


def single_view(request):
    return render(request, "travelista/blog/blog-single.html")


def home_view(request):
    return render(request, "travelista/blog/blog-home.html")
