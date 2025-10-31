from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.forms import NewsLetterForm


def home_view(request):
    if request.method == "POST":
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

    return render(request, "travelista/home/index.html")
