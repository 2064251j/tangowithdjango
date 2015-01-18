from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world! <br> <a href=\"about\">About</a>")

def about(request):
    return HttpResponse("This tutorial has been put together by Paulius Jonusas, 2064251j <br> <a href=\"./\">Go back</a>")
