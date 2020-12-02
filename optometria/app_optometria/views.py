from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django import forms

# Create your views here.


def index(request):
    return render(request, "inicio/index.html")


def medico(request):
    return render(request, "inicio/medico.html")


def secretaria(request):
    return render(request, "inicio/secretaria.html", {
        "pacientes": Paciente.objects.all(),
        "medicos": Medico.objects.all()
    })


def vendedor(request):
    return render(request, "inicio/vendedor.html")


def taller(request):
    return render(request, "inicio/taller.html")
