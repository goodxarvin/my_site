from django.shortcuts import render


def elements_main_page(request):
    return render(request, "travelista/elements.html")
