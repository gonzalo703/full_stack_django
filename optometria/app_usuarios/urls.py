from django.urls import path, include
from . import views


urlpatterns = [
    path("usuarios", views.usuarios, name="usuarios"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
]