from django.http import HttpResponse
from django.shortcuts import render


def index(reqest):
    # Construct a dictionary to pass to the template engine as its context
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier
    # Note that the first parameter is the template we wish to use.
    return render(reqest, 'rango/index.html', context=context_dict)


def about(reqest):
    context_dict = {'textblock': "This tutorial has been put together by Sergey."}

    return render(reqest, 'rango/about.html', context=context_dict)
