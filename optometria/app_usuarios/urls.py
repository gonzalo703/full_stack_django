from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("medico", views.medico, name="medico"),
    path("secretaria", views.secretaria, name="secretaria"),
    path("vendedor", views.vendedor, name="vendedor"),
    path("taller", views.taller, name="taller")
]
