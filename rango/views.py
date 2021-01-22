from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 

def index(request):
    # return HttpResponse("Rango says hey there partner! <a href='/rango/about'>Index</a>")
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    # return HttpResponse("Rango says here is the about page. <a href='/rango/'>About</a>")
    return render(request, 'rango/about.html', {})