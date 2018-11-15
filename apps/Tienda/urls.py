from django.urls import path
from apps.Tienda.views import index,categorias
from apps.Tienda.views import modificarProducto
from apps.Tienda.views import nuevoProducto
from apps.Tienda.views import eliminarProducto
from apps.Tienda.views import ProductoListView
from apps.Tienda.views import nuevaCategoria
from apps.Tienda.views import modificarCategoria
from apps.Tienda.views import eliminarCategoria
from apps.Tienda.views import ventas
from apps.Tienda.views import resumenVentas
from apps.Tienda.views import ventasBsq

app_name='tienda'
urlpatterns = [
   path('categorias',categorias,name="cat"),
   path('',index,name="index"),
   path('productos',ProductoListView.as_view(),name="prd"),
   path('nuevoProducto',nuevoProducto,name="nuevoPrd"),
   path('modProducto/<idProducto>',modificarProducto,name="modPrd"),
   path('eliminarProducto/<idProducto>',eliminarProducto,name="rmvPrd"),
   path('nuevaCategoria',nuevaCategoria,name="nuevaCat"),
   path('modCategoria/<idCategoria>',modificarCategoria,name="modCat"),
   path('rmvCategoria/<idCategoria>',eliminarCategoria,name="rmvCat"),
   path('ventas',ventas,name="ventas"),
   path('resumen/<idProducto>',resumenVentas,name="resumen"),
   path('busqueda',ventasBsq,name="ventasBsq"),
]
