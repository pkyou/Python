from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def HelloSite(resquest):
    return HttpResponse("<h1> Hello, my site by pk</h1>")