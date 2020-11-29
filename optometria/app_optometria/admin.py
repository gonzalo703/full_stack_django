from django.contrib import admin
from .models import Paciente, Medico, Turno, Historia_clinica
# Register your models here.

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Turno)
admin.site.register(Historia_clinica)
