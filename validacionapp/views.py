import fileinput
from django.shortcuts import render,request
from  django.http import HttpResponse
from django.core import  files
# Create your views here.

def validar(request):
    
    if request.files["val1", "val2"]:
        validar1=request.GET["val1"]
        validar2=request.GET["val2"]
        mensaje="Certificados correctos"
    else:
        mensaje= "certificados incorrectos"
    
    return render (request, "validacion.html", )
    