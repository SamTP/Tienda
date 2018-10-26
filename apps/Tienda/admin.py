from django.contrib import admin
from apps.Tienda.models import Categoria
from apps.Tienda.models import Producto
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)