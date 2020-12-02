from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("medico", views.medico, name="medico"),
    path("secretaria", views.secretaria, name="secretaria"),
    path("vendedor", views.vendedor, name="vendedor"),
    path("taller", views.taller, name="taller")
]
