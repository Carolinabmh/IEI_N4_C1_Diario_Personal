from django.shortcuts import render
from rest_framework import viewsets 

def error_404(request, exception):
    return render(request, '404.html', status=404)

#vista creada basada en funcion (FBV) para renderizar la pagina de inicio

def inicio(request):
    return render(request, 'inicio.html')

#vamos a crear una vista basada en clase (CBV) para renderizar la pagina de inicio 
from .models import Entrada, Categoria, Estado, HistorialEstado
from .serializer import EntradaSerializer, CategoriaSerializer, EstadoSerializer, HistorialEstadoSerializer

# Creación de vistas basadas en clases (CBV)

class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer


class HistorialEstadoViewSet(viewsets.ModelViewSet):
    queryset = HistorialEstado.objects.all()
    serializer_class = HistorialEstadoSerializer