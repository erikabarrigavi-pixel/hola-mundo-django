from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Hola_mundo(request):
    return HttpResponse("¡Hola mundo!")
