from django.shortcuts import render
from contact.forms import ContactForm
from django.contrib import messages


def contact_main_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            set_name_form = form.save(commit=False)
            set_name_form.name = "anonymous"
            messages.add_message(request, messages.SUCCESS, "request saved")
            set_name_form.save()
        else:
            messages.add_message(request, messages.ERROR,
                                 "request didn't saved")
    else:
        form = ContactForm()
    context = {"form": form}
    return render(request, "travelista/contact.html", context)
