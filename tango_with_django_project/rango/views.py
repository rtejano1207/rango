from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    # RRT 11.20.2015 - commented out so that I can try templates
    # return HttpResponse("Rango Says: Hello World! <br/><a href='/rango/about'>About</a>")

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
     context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
     return render(request, 'rango/index.html', context_dict)

def about(request):
    # construct own dictionary to pass to the template engine
    return HttpResponse("")

def about_template(request):
    #RRT 12.21.2015 - commented out so to try own template for about page

    # construct a dictionary to pass to the template engine as its context
    context_dict = {'italicmessage': "I am italicized font from the context"}

    # return a renedered response to send to the client
    # we make us of the shortcut function to make our lives easier.
    # note that the first parameter is that same {{ italicmessage }} in the template!
    return render(request, 'rango/about.html',context_dict)

