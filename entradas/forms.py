from django import forms
from . import models as mod


# Formulario de entradas
class EntradaForm(forms.ModelForm):
    class Meta:
        model = mod.Entrada

        fields = [
            'titulo',
            'contenido',
            'categoria',
            'estado',
            'es_publica',
            'habilitado'
        ]

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título de la entrada'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe aquí tu entrada',
                'rows': 6
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select'
            }),
            'es_publica': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'habilitado': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }


# Formulario de categorías
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = mod.Categoria

        fields = [
            'nombre',
            'descripcion',
            'habilitado'
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la categoría'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción de la categoría',
                'rows': 3
            }),
            'habilitado': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }


# Formulario de estados
class EstadoForm(forms.ModelForm):
    class Meta:
        model = mod.Estado

        fields = [
            'nombre',
            'descripcion',
            'habilitado'
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del estado'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del estado',
                'rows': 3
            }),
            'habilitado': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }


# Formulario del historial de estados
class HistorialEstadoForm(forms.ModelForm):
    class Meta:
        model = mod.HistorialEstado

        fields = [
            'entrada',
            'estado_anterior',
            'estado_nuevo'
        ]

        widgets = {
            'entrada': forms.Select(attrs={
                'class': 'form-select'
            }),
            'estado_anterior': forms.Select(attrs={
                'class': 'form-select'
            }),
            'estado_nuevo': forms.Select(attrs={
                'class': 'form-select'
            })
        }

    def __init__(self, *args, usuario=None, **kwargs):
        super().__init__(*args, **kwargs)

        if usuario is None or not usuario.is_authenticated:
            self.fields['entrada'].queryset = mod.Entrada.objects.none()

        elif not usuario.is_staff:
            self.fields['entrada'].queryset = mod.Entrada.objects.filter(
                usuario=usuario
            )
