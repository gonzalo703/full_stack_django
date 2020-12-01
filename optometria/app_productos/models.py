from django.db import models
from django.db.models import fields
from app_optometria.models import Paciente


# Create your models here.

class Tipo_lente(models.Model):
    derecha = models.BooleanField(default=False)
    izquierda = models.BooleanField(default=False)
    lejos = models.BooleanField(default=False)
    cerca = models.BooleanField(default=False)
    armazon = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.derecha} {self.lejos} {self.armazon}"


class Tipo_producto(models.Model):
    nombre = models.CharField(max_length=64)
    tipo_lente = models.ForeignKey(
        Tipo_lente, on_delete=models.CASCADE, related_name="lentes", null=True)

    def __str__(self):
        return f"{self.nombre}"


class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.ForeignKey(
        Tipo_producto, on_delete=models.CASCADE, related_name="categoria")

    def __str__(self):
        return f"{self.nombre}: {self.precio} {self.tipo}"


class Forma_pago(models.Model):
    forma_pago = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.forma_pago}"


class Estado(models.Model):
    estado = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.estado}"


class Pedido(models.Model):
    cantidad = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)
    producto = models.ManyToManyField(
        Producto, blank=True, related_name="productos")
    forma_pago = models.ForeignKey(
        Forma_pago, on_delete=models.CASCADE, related_name="pago")
    estado = models.ForeignKey(
        Estado, on_delete=models.CASCADE, related_name="estados")
    cliente = models.ForeignKey(
        Paciente, on_delete=models.CASCADE, related_name="cliente")

    def __str__(self):
        return f"{self.cliente}: {self.productos} {self.estados}"
