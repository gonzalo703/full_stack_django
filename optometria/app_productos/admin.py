from django.contrib import admin
from .models import Tipo_producto, Producto, Forma_pago, Estado, Pedido
# Register your models here.

admin.site.register(Producto)
admin.site.register(Tipo_producto)
admin.site.register(Forma_pago)
admin.site.register(Estado)
admin.site.register(Pedido)
