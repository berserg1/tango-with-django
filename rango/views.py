from django.http import HttpResponse


def index(reqest):
    html = "<html><body><p>Rango says hey there partner!</p><p><a href='/rango/about/'>About</a></p></body></html>"
    return HttpResponse(html)


def about(reqest):
    html = "<html><body><p>Rango says here is the about page</p><p><a href='/rango/'>Index</a></p></body></html>"
    return HttpResponse(html)
