from crypt import methods
from fileinput import filename
from tabnanny import filename_only
from django import apps
from django.shortcuts import render, redirect
from django.core.files import  FileSystemStorage

# Create your views here.

def validar(request):
    if request.method=='POST' and request.FILES['uploads']:
        uploads = request.FILES['uploads']
        fs=FileSystemStorage()
        filename= fs.save(uploads.name, uploads)
        uploaded_file_url=fs.url(filename)
        return render (request, 'validacion.html', {
            'uploaded_file_url': uploaded_file_url})
        
        
        
    return render (request, "validacion.html" )