from django.contrib import admin
from Dippitimer.models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Restaurante)
admin.site.register(MenuItem)
admin.site.register(Pedido)
admin.site.register(DescripcionPedido)
admin.site.register(Ingrediente)
admin.site.register(ListaIngredientes)
admin.site.register(Plato)