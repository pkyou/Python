from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import OutputString

def HelloSite(resquest):
    people = OutputString.People()

    age = people.age +12

    return HttpResponse("<h1> Hello, my site by pk %d </h1>"%age)