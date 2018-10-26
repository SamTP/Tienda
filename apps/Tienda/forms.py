from django import forms
from apps.Tienda.models import Producto
from apps.Tienda.models import Categoria

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto

        fields = [
            'nombre',
            'categoria',
            'descripcion',
            'costo',
            'disponible',
            'numExistencias',
        ]

        labels = {
            'nombre': 'Nombre',
            'categoria': 'Categoría',
            'descripcion': 'Descripción',
            'costo': 'Costo',
            'disponible': 'Disponible',
            'numExistencias': 'Número de Existencias',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'costo': forms.TextInput(attrs={'class':'form-control'}),
            'disponible': forms.CheckboxInput(attrs={'clas':'form-check-input'}),
            'numExistencias': forms.TextInput(attrs={'class':'form-control'}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria

        fields = [
            'nombre',
            'fechaCreacion',
        ]

        labels = {
            'nombre': 'Nombre',
            'fechaCreacion': 'Fecha Creación',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'fechaCreacion': forms.DateInput(attrs={'class':'form-control'}),
        }


