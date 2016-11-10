from django.http import HttpResponse


def index(reqest):
    return HttpResponse("Rango says hey there partner!")
