from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import OutputString

def HelloSite(resquest):
    people = OutputString.People()

    age = '%d'%people.age
    return HttpResponse("<h1> Hello, my site by pk </h1>"+age)