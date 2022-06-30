from django.shortcuts import render, redirect


# Create your views here.

def validar(request):
   
    return render (request, "validacion.html" )