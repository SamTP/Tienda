from django.db import models
# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    fechaCreacion=models.DateField(default='2000-01-01')


class Producto(models.Model):
    categoria = models.ForeignKey(
        Categoria, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=75)
    costo = models.DecimalField(decimal_places=2, max_digits=15)
    disponible = models.BooleanField()
    numExistencias = models.IntegerField()

class Ventas(models.Model):
    # producto=models.ForeignKey(
    #     Producto,blank=True, null=True,on_delete=models.CASCADE)
    producto=models.CharField(max_length=75,default=" ")
    precio=models.DecimalField(decimal_places=2,max_digits=15,default=0)
    cantidad=models.IntegerField(default=0)
    total=models.DecimalField(decimal_places=2,max_digits=15,default=0)


