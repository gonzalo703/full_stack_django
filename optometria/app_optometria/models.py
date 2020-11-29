from django.db import models

# Create your models here.


class Paciente(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.id}: {self.nombre} {self.apellido}"


class Medico(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id}: {self.nombre} {self.apellido}"


class Turno(models.Model):
    medico = models.ForeignKey(
        Medico, on_delete=models.CASCADE, related_name="medico")
    paciente = models.ForeignKey(
        Paciente, on_delete=models.CASCADE, related_name="paciente")
    fecha_turno = models.DateTimeField()

    def __str__(self):
        return f"{self.paciente}: {self.medico} {self.fecha_turno} horas"


class Historia_clinica(models.Model):
    medico = models.ForeignKey(
        Medico, on_delete=models.CASCADE, related_name="medicos")
    paciente = models.ForeignKey(
        Paciente, on_delete=models.CASCADE, related_name="pacientes")
    historia_clinica = models.CharField(max_length=500)
