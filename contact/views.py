from django.shortcuts import render
from contact.forms import ContactForm


def contact_main_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    context = {"form": form}
    return render(request, "travelista/contact.html", context)
