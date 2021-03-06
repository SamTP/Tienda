from django.shortcuts import render,redirect
from apps.Tienda.models import Categoria
from apps.Tienda.models import Producto
from apps.Tienda.models import Ventas
from django.views.generic import ListView
from apps.Tienda.forms import ProductoForm
from apps.Tienda.forms import CategoriaForm
from apps.Tienda.forms import Venta
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'base/index.html')


# Ventas de Productos


def ventas(request):
    context = {'productos': Producto.objects.all()}
    return render(request,'Tienda/ventas.html',context)

def ventasBsq(request):
    nombrePrd=request.GET.get('campo')
    context = {'productos': Producto.objects.filter(nombre=nombrePrd)}
    return render(request,'Tienda/ventasBsq.html',context)


def resumenVentas(request,idProducto):
    producto=Producto.objects.get(id=idProducto)
    total=0*producto.costo
    nombre=producto.nombre+" "+producto.descripcion
    costo=producto.costo
    if request.method=='POST':
        form = Venta(request.POST,initial={'producto':nombre,'cantidad':0,'total':total,'precio':costo})
        if form.is_valid():
            resta=form.cleaned_data['cantidad']
            if(resta>producto.numExistencias):
                messages.error(request," No hay sificiente producto en inventario para esa compra")
                return render(request, 'Tienda/resumenVenta.html',{'form':form})
            else:
                messages.success(request,"Venta exitosa")
                producto.numExistencias=producto.numExistencias-resta
                if(producto.numExistencias==0):
                    producto.disponible=False
                producto.save()
                form.save()
        return redirect('tienda:prd')
    else:
        form = Venta(initial={'producto':nombre,'cantidad':0,'total':total,'precio':costo})
    return render(request, 'Tienda/resumenVenta.html',{'form':form})

#Categorías


def categorias(request):
    context = {'categorias': Categoria.objects.all()}
    return render(request, 'Tienda/cat.html', context)

def nuevaCategoria(request):
    if request.method=='POST':
        form=CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('tienda:cat')
    else:
        form=CategoriaForm()
    return render(request, 'Tienda/FormCat.html',{'form':form})

def modificarCategoria(request,idCategoria):
    categoria=Categoria.objects.get(id=idCategoria)
    if(request.method=="GET"):
        form = CategoriaForm(instance=categoria)
    else:
        form = CategoriaForm(request.POST,instance=categoria)
        if form.is_valid():
            form.save()
        return redirect('tienda:cat')
    return render(request, 'Tienda/FormCat.html',{'form':form})

def eliminarCategoria(request,idCategoria):
    categoria= Categoria.objects.get(id=idCategoria)
    categoria.delete()
    return redirect('tienda:cat')

# Productos

def nuevoProducto(request):
    if request.method=='POST':
        form=ProductoForm(request.POST)
        if form.is_valid():
        form.save()
        return redirect('tienda:prd')
    else:
        form=ProductoForm()
    return render(request, 'Tienda/FormPrd.html',{'form':form})

def modificarProducto(request,idProducto):
    producto=Producto.objects.get(id=idProducto)
    if(request.method=="GET"):
        form = ProductoForm(instance=producto)
    else:
        form = ProductoForm(request.POST,instance=producto)
        if form.is_valid():
            form.save()
        return redirect('tienda:prd')
    return render(request, 'Tienda/FormPrd.html',{'form':form})

def eliminarProducto(request,idProducto):
    producto = Producto.objects.get(id=idProducto)
    producto.delete()
    return redirect('tienda:prd')

class ProductoListView(ListView):
    model = Producto
    queryset=Producto.objects.all()  
    template_name = "Tienda/productos.html"





