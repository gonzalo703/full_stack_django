from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def usuarios(request):
    return render(request, "usuarios/usuarios.html")
