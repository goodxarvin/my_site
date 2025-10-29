from django.shortcuts import render


def contact_main_page(request):
    if request.method == "POST":
        print(request.POST.get("name"))
    return render(request, "travelista/contact.html")
