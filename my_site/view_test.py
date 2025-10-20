from django.http import HttpResponse, JsonResponse


def tset_request(request):
    return HttpResponse("<b><h1>test successful :)<h1><b>")


def test_json(request):
    return JsonResponse({"json": "successful"})
